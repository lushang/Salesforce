import requests
import json
import time
from bs4 import BeautifulSoup
import re

# This module fetch all Lightning Aura Components from `Salesforce Lightning Component Library`,
# then structure a tag_definition for haoIde completion

base_url = 'https://developer.salesforce.com/docs/component-library/aura'
name_spaces = ['lightning', 'aura', 'forceChatter', 'ui', 'forceCommunity', 'wave', 'lightningsnapin',
               'force', 'clients', 'ltng', 'lightningcommunity', 'flexipage']
def_types = ['component', 'event', 'interface', 'module']


def get_all_cmps():
    """
    Get all Lighting Bundle List
    :return: bundle list, including aura and lwc
    """
    form_data = {
        'message': '{"actions":[{"id":"62;a","descriptor":"serviceComponent://ui.lightning.docs.components.aura.components.controllers.ComponentLibraryDataProviderController/ACTION$getBundleDefinitionsList","callingDescriptor":"UNKNOWN","params":{},"storable":true}]}',
        'aura.context': '{"mode":"PROD","fwuid":"99z7fRM0JVFD9-eSEIj7gQ","app":"componentReference:offCoreSuite","loaded":{"APPLICATION@markup://componentReference:offCoreSuite":"Yn83Zqqg1Wy3p0F9mjBwgQ"},"dn":[],"globals":{},"uad":false}',
        'aura.token': 'aura'
    }
    time1 = time.time()
    print('start time', time1)
    r = requests.post(base_url, form_data, timeout=20)
    res_json = json.loads(r.text, encoding=r.encoding)
    all_cmps = get_return_value(res_json)
    print('end time', (time.time() - time1))

    def_types = []
    namespace = []
    components = []
    events = []
    interfaces = []
    modules = []
    for k, v in all_cmps.items():
        def_type = v.get('defType')
        if def_type not in def_types:
            def_types.append(def_type)
        if v.get('namespace') not in namespace:
            namespace.append(v.get('namespace'))
        if def_type == 'component':
            components.append(k)
        elif def_type == 'event':
            events.append(k)
        elif def_type == 'interface':
            interfaces.append(k)
        elif def_type == 'module':
            modules.append(k)

    components.sort()
    events.sort()
    interfaces.sort()
    modules.sort()
    # print('res json keys', all_cmps.keys())
    # print('def type', def_types)
    # print('namespace', namespace)
    # print('components', components)
    # print('events', json.dumps(events))
    # print('interfaces', json.dumps(interfaces))
    # print('modues', modules)

    # return all_cmps
    return components, events, interfaces, modules


def get_cmp(cmp_name):
    message = '{"actions":[{"id":"1;a","descriptor":"serviceComponent://ui.lightning.docs.components.aura.components.controllers.ComponentLibraryDataProviderController/ACTION$getBundleDefinition","callingDescriptor":"UNKNOWN","params":{"descriptor":"cmp_name"},"storable":true}]}'
    form_data = {
        'message': message.replace('cmp_name', cmp_name),
        'aura.context': '{"mode":"PROD","fwuid":"99z7fRM0JVFD9-eSEIj7gQ","app":"componentReference:offCoreSuite","loaded":{"APPLICATION@markup://componentReference:offCoreSuite":"Yn83Zqqg1Wy3p0F9mjBwgQ"},"dn":[],"globals":{},"uad":false}',
        'aura.token': 'aura'
    }
    time1 = time.time()
    r = requests.post(base_url, form_data, timeout=20)
    print('fetch time %.3f with: ' % (time.time() - time1), cmp_name)
    res_json = json.loads(r.text, encoding=r.encoding)
    cmp_def = get_return_value(res_json)
    # print('cmp def desc', cmp_def)
    return cmp_def


def get_return_value(res_json):
    return_value = None
    if 'actions' in res_json:
        actions = res_json.get('actions')
        if len(actions) >= 1:
            action = actions[0]
            return_value = action.get('returnValue')
    return return_value


def parse_cmp(cmps):
    with open('old_aura.json', 'r', encoding='utf-8') as old_f:
        old_dict = json.load(old_f)
        print('old size: ', len(old_dict))
        aura_dict = {}
        for cmp_name in cmps:
            cmp_def = get_cmp(cmp_name)
            attr_dict = {}
            cmp = {}
            if cmp_name in old_dict:
                cmp = old_dict[cmp_name]

            else:
                cmp['attribs'] = {}
                cmp['simple'] = False
                cmp['type'] = 'aura' if cmp_def.get('defType') == 'component' else 'lwc'

            cmp['description'] = cmp_def.get('description')
            cmp['access'] = cmp_def.get('access')

            for attr_def in cmp_def.get('attributes'):
                attr_name = attr_def.get('name')
                if attr_name in cmp['attribs']:
                    attr = cmp['attribs'].get(attr_name)
                    # print('attr', attr)
                    if 'description' not in attr:
                        attr['description'] = attr_def.get('description')
                else:
                    attr = {
                        # 'name': attr_def.get('name'),
                        'type': attr_def.get('type'),
                        'description': attr_def.get('description')
                    }
                attr['access'] = attr_def.get('access')
                attr['required'] = attr_def.get('required')

                attr_dict[attr_name] = attr

            # add old attributes
            for attr_name in cmp['attribs']:
                if attr_name not in attr_dict:
                    attr_dict[attr_name] = cmp['attribs'].get(attr_name)

            cmp['attribs'] = attr_dict
            aura_dict[cmp_name] = cmp

        # add old cmps
        for cmp_name in old_dict:
            if cmp_name not in aura_dict:
                aura_dict[cmp_name] = old_dict.get(cmp_name)

        print('combine size: ', len(aura_dict))
        with open('aura.json', 'w', encoding='utf-8') as f:
            json.dump(aura_dict, f, indent=4)
        print('finished!\n')


def parse_event(events):
    evt_dict = {}
    for evt in events:
        evt_def = get_cmp(evt)
        evt_dict[evt] = {
            'attrs': [],
            'eventType': evt_def.get('eventType'),
            'access': evt_def.get('access'),
            'description': evt_def.get('description')
        }
        for attr in evt_def.get('attributes'):
            evt_dict[evt]['attrs'].append({
                'name': attr.get('name'),
                'type': attr.get('type'),
                'access': attr.get('access'),
                'required': attr.get('required'),
                'description': attr.get('description')
            })
    with open('events.json', 'w', encoding='utf-8') as f:
        json.dump(evt_dict, f, indent=4)
    print('finished!\n')


if __name__ == '__main__':
    (components, events, interfaces, modules) = get_all_cmps()
    # print('components size: ', len(components))
    # print('events size: ', len(events))
    # print('interfaces size: ', len(interfaces))
    # print('modules size: ', len(modules))
    print('aura + lwc size: ', len(components + modules))
    parse_cmp(components + modules)
    # cmp_def = get_cmp('lightning:buttonStateful')
    # print('lightning:buttonStateful: ', json.dumps(cmp_def))
    # with open('old_aura.json', 'r', encoding='utf-8') as old_f:
    #     old_dict = json.load(old_f)
    #     print('old size: ', len(old_dict))
    # with open('aura.json', 'r', encoding='utf-8') as aura_f:
    #     aura_dict = json.load(aura_f)
    #     print('aura size: ', len(aura_dict))
    #     for key in aura_dict:
    #         if 'simple' not in aura_dict[key]:
    #             aura_dict[key]['simple'] = False
    #         if 'type' not in aura_dict[key]:
    #             aura_dict[key]['type'] = 'aura'
    #     # with open('new_aura.json', 'w', encoding='utf-8') as new_f:
    #     #     json.dump(aura_dict, new_f, indent=4)
