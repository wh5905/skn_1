import PySimpleGUI as sg
import os.path


class Mainv:
    def __init__(self):
        left_col = [
            [
                sg.Text("이미지가 들어있는 폴더를 선택해주세요"),
                sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse(button_text="열기"),
            ],
            [
                sg.Listbox(
                    values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
                )
            ],
        ]

        image_col = [
            [sg.Text("선택한 폴더의 이미지 리스트")],
            [sg.Text(size=(40, 1), key="-TOUT-")],
            [sg.Image(key="-IMAGE-")],
        ]

        layout = [[sg.Column(left_col), sg.VSeparator(), sg.Column(image_col)]]

        window = sg.Window("이미지뷰어", layout)

        while True:
            event, values = window.read()

            if event in (None, "Exit"):
                break
            if event == "-FOLDER-":
                folder = values["-FOLDER-"]
                try:
                    file_list = os.listdir(folder)
                    # print(file_list)
                except Exception as e:
                    print(e)
                    file_list = []
                fnames = [
                    f
                    for f in file_list
                    if os.path.isfile(os.path.join(folder, f))
                    and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp"))
                ]

                window["-FILE LIST-"].update(fnames)
            # 테이블객체로 리스트업
            elif event == "-FILE LIST-":
                try:
                    filename = os.path.join(
                        values["-FOLDER-"], values["-FILE LIST-"][0]
                    )
                    window["-TOUT-"].update(filename)
                    window["-IMAGE-"].update(filename=filename)
                except Exception as e:
                    print(e)
                    pass

        window.close()