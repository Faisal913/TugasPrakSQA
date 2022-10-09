from xml.dom.minidom import parse
matkul = parse('matkul.xml') 
nilaiMatkul = matkul.getElementsByTagName("nilaimatkul")[0].firstChild.nodeValue 
jumlahItem = len(nilaiMatkul)
i = 0
while i <= jumlahItem :
    namaMatkul = matkul.getElementsByTagName("NamaMatkul")[i].firstChild.nodeValue 
    nilaiAngka = matkul.getElementsByTagName("NilaiAngka")[i].firstChild.nodeValue 
    nilaiHuruf = matkul.getElementsByTagName("NilaiHuruf")[i].firstChild.nodeValue 
    print("Nama Matakuliah : " , namaMatkul) 
    print("Nilai Angka : " , nilaiAngka) 
    print("Nilai Huruf : " , nilaiHuruf)
    i = i + 1