import os

jpg_path = 'C:/Users/ADMIN/yolov3/data/images/plate/images'
txt_path = 'C:/Users/ADMIN/yolov3/data/images/plate/labels'
txt_list = os.listdir(txt_path)
jpg_list = os.listdir(jpg_path)

search = "._"
input_txt = ".txt"
input_jpg = ".jpg"
new_txt = []
new_jpg = []
new_jpg_2 = []
txt = "."
jpg = ""
s = set()

def make_new_list():
    for i in range(len(txt_list)):
        if txt_list[i][0] == '.' and txt_list[i][1] == '_':
            print("except jpg ._ in head")
        elif input_txt not in txt_list[i]:
            print("except no txt")
        else:
            new_txt.append(txt_list[i])

    for i in range(len(jpg_list)):
        if jpg_list[i][0] == '.' and jpg_list[i][1] == '_':
            print("except jpg ._ in head")
        elif input_jpg not in jpg_list[i]:
            print("except no jpg")
        else:
            new_jpg.append(jpg_list[i])


def number_of_file():
    if len(new_txt) == len(new_jpg):
        print("파일의 수는 ", len(new_txt), "로 같습니다.")
    else:
        print("파일의 수가 다릅니다. 직접 세주세요")


def ready_to_compare():
    for i in range(len(new_txt)):
        txt = new_txt[i]
        txt = txt.replace(".txt", "")
        jpg = new_jpg[i]
        jpg = jpg.replace(".jpg", "")
        s.add(txt)
        new_jpg_2.append(jpg)


def print_difference():
    j = 0
    for i in range(len(new_jpg_2)):
        if new_jpg_2[i] in s:
            j = j + 1
        else:
            print("txt와 일치하지 않는 jpg파일의 이름은 : ", new_jpg_2[i])
    return j


def print_result(j):
    if j == len(new_txt):
        print("문자열이 모두 일치합니다. 총 검사 수 : ", j)
    else:
        print("일치하지 않는 문자열이 존재합니다.")


def main() :
    print("초기 전체 txt파일 수 : ", len(txt_list))
    print("초기 전체 jpg파일 수 : ", len(jpg_list))

    make_new_list()

    print("제외사항 제외후 새로 생성한 txt파일 수 : ", len(new_txt))
    print("제외사항 제외후 새로 생성한 jpg파일 수 : ", len(new_jpg))

    number_of_file()
    ready_to_compare()
    correct = print_difference()
    print_result(correct)


if __name__ == "__main__":
    main()