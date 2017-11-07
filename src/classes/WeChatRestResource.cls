/**********************************************************************
 * 
 *
 * @url: /services/apexrest/WeChat/*
 * @data:
 *  {
        communicate with WeChat via multiple WeChat Account
    }
*************************************************************************/
@RestResource(urlMapping = '/WeChat/*')
global class WeChatRestResource {

    @HttpGet
    global static void doGet () {

        // Gets the verification parameters from WeChat request
        String signature = RestContext.request.params.get('signature');
        String timestamp = RestContext.request.params.get('timestamp');
        String nonce = RestContext.request.params.get('nonce');
        String echostr = RestContext.request.params.get('echostr');
        String path = RestContext.request.requestURI;

        // Gets the Default WeChat setting from custom setting
        WeChatSettings__c weChatSetting = WeChatUtil.weChatSetting;

        // If the request is for AI account, use the AI custom setting
        if (path.contains(WeChatConfig.AI)) {
            weChatSetting = WeChatUtil.wcAISetting;
        }

        // Verifies the signature make sure the GET request from WeChat, if that return the echostr
        // else verification failed.
        if (GenerateSignature(weChatSetting.Token__c, timestamp, nonce) == signature) {
            RestContext.response.addHeader('Content-Type', 'text/plain');
            RestContext.response.responseBody = Blob.valueof(echostr);
        }
    }

    /*
     * 1) The dictionary order sorting of token, timestamps and nonce three parameters
     * 2) Takes three parameters string spliced into a string SHA1 encryption
     * 3) Compares the encrypted string with the signature that identifies the request comes from the WeChat
     */
    public static String GenerateSignature (String token, String timestamp, String nonce) {


        List<String> SignatureStringList = new List<String> { token, timestamp, nonce };
        SignatureStringList.sort();

        String content = '';
        for (String s : SignatureStringList) {
            content += s;
        }

        Blob hash = Crypto.generateDigest('SHA1', Blob.valueOf(content));
        String hexHash = EncodingUtil.convertToHex(hash);
        // System.debug(LoggingLevel.INFO, '*** hexHash: ' + hexHash);
        return hexHash;
    }

    @HttpPost
    global static void doPost () {

        RestRequest req = RestContext.request;
        RestResponse res = RestContext.response;

        String XmlMessage = req.requestBody.toString();
        System.debug(LoggingLevel.INFO, '*** XmlMessage: ' + XmlMessage);

        // URL encoding
        XmlMessage = EncodingUtil.urlEncode(XmlMessage,'UTF-8');

        // Removes i.e. '<![CDATA['
        XmlMessage = XmlMessage.replaceAll('%3C%21%5BCDATA%5B', '');

        // Removes ']]>'
        XmlMessage = XmlMessage.replaceAll('%5D%5D%3E', '');

        // URL decoding
        XmlMessage = EncodingUtil.urlDecode(XmlMessage,'UTF-8');
        System.debug(LoggingLevel.INFO, '*** New XmlMessage: ' + XmlMessage);

        Dom.Document doc = new Dom.Document();
        doc.load(XmlMessage);
        Dom.XMLNode xml = doc.getRootElement();
        System.debug(LoggingLevel.DEBUG, '*** xml: ' + xml);

        String responseCotent = WeChatResponse.createResponseCotent(xml);
        // String responseCotent = '';
        res.addHeader('Content-Type', 'text/plain');
        res.responseBody = Blob.valueOf(responseCotent);
        // Logger.log('WeChatRestResource', 'Post data from WeChat', XmlMessage);
    }
}