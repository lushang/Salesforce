# Use this file to parse biubiu

import csv

def labparse(**args):
    newfile = open('labs_e.csv', 'w', newline='')
    writer = csv.writer(newfile)
    with open('labs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            # print(len(row))
            labs = []
            if (row[11] == 'Y'):
                labs.extend(['SOTC', 'Waigaoqiao Lab'])
            if (row[12] == 'Y'):
                labs.extend(['Nantong Lab', 'Deqiao Lab'])
            if(row[13] == 'Y'):
                labs.extend(['Jiangyin Lab'])
            # NJ
            if (row[14] == 'Y') :
                labs.extend(['Nanjing Lab'])
            if (row[15] == 'Y') :
                labs.extend(['Zhangjiagang Lab'])
            # Shekou Lab
            # if (row[16] == 'Y') :
            #     labs.extend(['Shekou Lab'])
            # if (row[17] == 'Y') :
            #     labs.extend([])
            # Zhuhai Lab
            if (row[18] == 'Y') :
                labs.extend(['Zhuhai Lab'])
            if (row[19] == 'Y') :
                labs.extend(['Dongguan Lab'])
            if (row[20] == 'Y') :
                labs.extend(['Huizhou Lab'])
            if (row[21] == 'Y') :
                labs.extend(['Hainan Vopak Lab'])
            if (row[22] == 'Y') :
                labs.extend(['Tianjin Lab'])
            if (row[23] == 'Y') :
                labs.extend(['Dalian Lab'])
            # qinghuangdao lab
            # if (row[24] == 'Y') :
            #     labs.extend([])
            if (row[25] == 'Y') :
                labs.extend(['Qingdao Lab'])
            if (row[26] == 'Y') :
                labs.extend(['Zhapu Lab'])
            if (row[27] == 'Y') :
                labs.extend(['Ningbo Lab'])
            
            if (len(labs) > 0) :
                row.append(';'.join(labs))
            writer.writerow(row)
    newfile.close()
    
if __name__ == '__main__':
    labparse()