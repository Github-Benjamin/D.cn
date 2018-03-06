def CreateDATA(filename):
    listdata = []
    files = file(str(filename), "r")
    for i in files.readlines():
        listdata.append(i.split()[1])
    return listdata

cpu_list = CreateDATA("QiBin/cpu_com_droidhang_ad.txt")
pss_list = CreateDATA("QiBin/pss.txt")
fps_list = CreateDATA("QiBin/fps.txt")