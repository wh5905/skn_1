import PySimpleGUI as sg
import os.path
from glob import glob


class MainView:
    def __init__(self):

        left_col = [
            [
                sg.Text("이미지가 들어있는 폴더를 선택해주세요."),
                sg.In(size=(25, 1), enable_events=True, key="-Folder-"),
                sg.FolderBrowse(button_text="폴더 선택"),
            ],
            [
                sg.Listbox(
                    values=[],
                    enable_events=True,
                    size=(40, 20),
                    key="-FILE LIST-",
                )
            ],
        ]

        image_col = [
            [sg.Text("선택한 이미지 리스트")],
            [sg.In(size=(40, 1), key="-TOUT-")],
            [sg.Image(key="-IMAGE-")],
        ]
        layout = [
            [
                sg.Menu(
                    [
                        ["File", ["Open", "Save", "Exit"]],
                        [
                            "Edit",
                            [
                                "Paste",
                                [
                                    "Special",
                                    "Normal",
                                ],
                                "Undo",
                            ],
                        ],
                    ]
                ),
            ],
            [sg.Column(left_col), sg.VSeperator(), sg.Column(image_col)],
        ]

        window = sg.Window("이미지뷰어", layout)
        window.Finalize()
        window.Maximize()

        while True:
            event, values = window.read()

            if event in (None, "Exit"):
                break
            if event == "-Folder-":
                folder = values["-Folder-"]  # folder > 파일 경로 문자열
                try:
                    file_list = os.listdir(folder)
                except Exception as e:
                    print(e)
                    file_list = []

                fnames = [
                    f
                    for f in file_list
                    if os.path.isfile(
                        os.path.join(folder, f)
                    )  # 경로와 파일명을 합쳐서 파일이 있는지 확인
                    and f.lower().endswith((".png", ".gif", ".jpg", ".jpeg"))
                ]
                # fnames = glob(f"{folder}/**/*.png", recursive=True)
                 

                # myExt = ["*.png", "*.jpeg", "*.jpg", "*.gif"]
                # fnames = glob(r"C:\Users\USER\Desktop/Downlooads\**/*.png", recursive=True),
                # print(fnames)

                # glob
                # 리스트업 table
                # 최대화면

                window["-FILE LIST-"].update(fnames)

            elif event == "-FILE LIST-":  # 이미지 리스트에서 선택한 이미지를 보여줌
                try:
                    filename = os.path.join(
                        values["-Folder-"], values["-FILE LIST-"][0]
                    )
                    window["-TOUT-"].update(filename)
                    window["-IMAGE-"].update(filename=filename)
                except Exception as e:
                    print(e)
                    pass

        window.close()
