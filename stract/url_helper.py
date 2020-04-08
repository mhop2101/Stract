# Input https://www.fincaraiz.com.co/apartamentos/venta/bella-suiza/bogota/?ad=30|1||||1||8|||67|3630001|3630101|||||||||||||||1|||1||griddate%20desc|||bella+suiza|-1||
# Output:
# https://www.fincaraiz.com.co/apartamentos/venta/bella-suiza/bogota/?ad=30|1||||1||8|||67|3630001|3630101|||||||||||||||1|||1||griddate%20desc|||bella+suiza|-1||
# https://www.fincaraiz.com.co/apartamentos/venta/bella-suiza/bogota/?ad=30|{}||||1||8|||67|3630001|3630101|||||||||||||||1|||1||griddate%20desc|||bella+suiza|-1||

def url_parser(url):
    url = list(url)
    index = find_index_of_first_pipe(url)
    second_list= url[index:]
    first_list= url[:index]
    second_list[0] = "{}"
    final_1 = listToString(first_list)
    final_2 = listToString(second_list)
    return final_1 + final_2

def find_index_of_first_pipe(list):
    for i in range(len(list)):
        if list[i] == '|':
            return i + 1

def listToString(s):
    str1 = ""
    return (str1.join(s))

def retrieve_relevant_info(url):
    try:
        url = url.split("/")
        relevant = url[3] + "_" + url[4] + "_" + url[5] + "_" + url[6] + "_"
        return relevant
    except:
        return "StractResults"


if __name__ == "__main__":
    print("https://www.fincaraiz.com.co/apartamentos/venta/bella-suiza/bogota/?ad=30|1||||1||8|||67|3630001|3630101|||||||||||||||1|||1||griddate%20desc|||bella+suiza|-1||"+"\n\n")
    print(url_parser("https://www.fincaraiz.com.co/apartamentos/venta/bella-suiza/bogota/?ad=30|1||||1||8|||67|3630001|3630101|||||||||||||||1|||1||griddate%20desc|||bella+suiza|-1||"))
    print(retrieve_relevant_info("https://www.fincaraiz.com.co/apartamentos/venta/bella-suiza/bogota/?ad=30|1||||1||8|||67|3630001|3630101|||||||||||||||1|||1||griddate%20desc|||bella+suiza|-1||"+"\n\n"))
