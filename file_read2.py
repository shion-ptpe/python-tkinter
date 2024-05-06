import tkinter as tk
import os  # 現在のディレクトリを取得するのに使っている
from tkinter import filedialog  # ファイルダイアログを開くためのモジュール
import sys
import webbrowser

class File_Selection(tk.Frame):
    def __init__(self, root):   # ファイル選択のボタンを作る
        super().__init__(root)  # super()でtk.Frameが呼ばれる(フレームが作られる)
        self.pack()
        global file_name
        global file_content
        global file_name_lists
        global file_content_lists
        file_content=""
        file_name_lists=[]
        file_content_lists=[]
    def Make_button(self):
        file_button = tk.Button(self, text="ファイルを追加する",relief=tk.RAISED, cursor="hand2",font=("normal","25"))
        file_button.pack()
        file_button.bind("<ButtonPress>", File_Selection.file_add)
        file_button.bind("<ButtonPress>", File_Selection.lists_button,"+")

    def file_add(event):
        global file_name
        global file_content
        typ = [("","*py")]  # 拡張子がpyのファイルのみ選択; 「＊」は任意の0文字以上を表すワイルドカード
        dir = os.path.abspath(os.path.dirname(__file__))  # 今いるファイルの場所（__file__）からフォルダ名を参照し（os.path.dirname()）、このフォルダ名(今は相対パス)を絶対パスに変換
        path = filedialog.askopenfilename(filetypes = typ, initialdir = dir)  # ファイルダイアログを表示する。
        if path  == "":
            print("\nファイルを読み込みませんでした。\n")
            return 0
        print("\n"+path+"を選択しました。\n")  # ファイルのパスが取得できる 
        file_name=os.path.basename(path)
        if (file_name in file_name_lists)==False:   # 指定の値と同じ要素がリストに何個含まれているか取得する
            with open(path) as f:
                file_content = f.read()
                file_content_lists.append(file_content)
                file_name_lists.append(file_name)
        elif (file_name in file_name_lists)==True:
            file_name = ""
        else:
            print("\nエラーが起きました。\n")
        return 

    # ファイル一覧をボタンで表示する。
    def lists_button(event):
        if file_name == "":
            print("既に選択されているファイルです。")
        else:
            print(file_name_lists)
            bt = tk.Button(frame_scrollbar_list, text=file_name)
            bt.bind("<ButtonPress>", File_Selection.content_button)
            bt.pack(fill=tk.X) # file_button.bind("<ButtonPress>", File_Selection.content_button,"+")
        
    # ファイルの中身を表示する部分    
    def content_button(event):
        file_name_copy=file_name
        file_content_copy=file_content  # file_contentのまま代入するとボタンごとにラベルを付けられない
        la_name =tk.Label(frame_scrollbar_content,text="\n----------------"+file_name_copy+"----------------\n")
        la_content = tk.Label(frame_scrollbar_content,text=file_content_copy)
        la_name.pack()
        la_content.pack()
        another.deiconify()


    def Make_Scrollbar_lists(self):
        global canvas1
        global frame_scrollbar_list 
        canvas1=tk.Canvas(self, width=300, height=300,scrollregion=(0,0,300,500))  # scrollregioはスクロール時の描画
        canvas1.pack(side=tk.LEFT, fill=tk.BOTH)
        ybar = tk.Scrollbar(self, orient=tk.VERTICAL)  
        ybar.pack(side=tk.LEFT, fill=tk.Y)  # スクロールバーを上下いっぱいに引き伸ばす
        ybar.config(command=canvas1.yview)  # キャンバスの表示領域が自動的に変化
        canvas1.config(yscrollcommand=ybar.set)  # キャンバススクロール時にスクロールバーのスライダーも動くようにする
        # FrameウィジェットはScrollbarに対応していないため、フレームを重ねなければならない
        frame_scrollbar_list= tk.Frame(canvas1)
        canvas1.create_window((0,0), window=frame_scrollbar_list, anchor=tk.NW, width=canvas1.cget('width')) # frameのウィジェットをCanvas上に作成。


class Make_Scrollbar_config(tk.Frame):
    def __init__(self, another):   # ファイル選択のボタンを作る
        super().__init__(another,background="#ededed")  # super()でtk.Frameが呼ばれる(フレームが作られる)
        self.pack(side=tk.LEFT)

    def Make_Scrollbar_content(self):
        global canvas2
        global frame_scrollbar_content
        canvas2=tk.Canvas(self, width=1300, height=700,scrollregion=(0,0,15000,15000))  # scrollregioはスクロール時の描画
        canvas2.grid(row=0, column=3)
        xbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        ybar = tk.Scrollbar(self, orient=tk.VERTICAL)  
        xbar.grid(row=1, column=3, sticky=tk.W + tk.E) # スクロールバーを上下いっぱいに引き伸ばす
        ybar.grid(row=0, column=4, sticky=tk.N + tk.S)
        xbar.config(command=canvas2.xview)
        ybar.config(command=canvas2.yview)  # キャンバスの表示領域が自動的に変化
        canvas2.config(xscrollcommand=xbar.set)
        canvas2.config(yscrollcommand=ybar.set)  # キャンバススクロール時にスクロールバーのスライダーも動くようにする        # FrameウィジェットはScrollbarに対応していないため、フレームを重ねなければならない
        frame_scrollbar_content= tk.Frame(canvas2)
        canvas2.create_window((0,0), window=frame_scrollbar_content, anchor=tk.NW) # frameのウィジェットをCanvas上に作成。

class References_Link(tk.Frame):
    def __init__(self, root):
        # 参考文献--------------------------------------------------------------
        super().__init__(root)  # super()でtk.Frameが呼ばれる(フレームが作られる)
        self.pack()
        self.pack(side = tk.LEFT, anchor=tk.S)
        self.link_References = tk.Label(self,text="参考文献")
        # ハイパーリンクを作る関数を呼び出す
        self.make_link("Tkinterの使い方：スクロールバー（Scrollbar）の使い方","https://daeudaeu.com/scrollbar/")
        self.make_link("Pythonのクラス（class）の基本を徹底解説、具体的な書き方も","https://camp.trainocate.co.jp/magazine/python-class/")
        self.make_link("Tkinterでスクロールバーを作りたい - Teratail","https://teratail.com/questions/149640")
        self.make_link("【Python tkinter】Scrollbar（スクロールバー）ウィジェットを作成・配置する方法","https://office54.net/python/tkinter/python-tkinter-scrollbar")
        self.make_link("【Tkinter】bindメソッドによるトリガーイベントとコールバック関数の紐づけ","https://denno-sekai.com/tkinter-bind/")
        self.make_link("Python でファイル選択画面を表示する","https://daeudaeu.com/python_filedialog/")
        # self.make_link("","")
        self.link_References.pack(side =tk.BOTTOM, anchor=tk.W)

    # 参考文献のリンク作成の関数
    def jump_to_link(self, url):  # urlクリック時の動作を定義
        webbrowser.open_new(url)
    def make_link(self, link_title, Destination):
        link_wid = tk.Button(self,text=link_title, foreground="#346592", activeforeground="#734898", cursor="hand2")
        link_wid.bind("<ButtonPress>", lambda e:self.jump_to_link(Destination))
        link_wid.pack(side =tk.BOTTOM,anchor=tk.W) 



if __name__ == '__main__':
    global another    
    root = tk.Tk()
    root.title("ファイル内容をウィジェット上に表示する")
    root.geometry("600x600")

    another = tk.Tk()
    another.title("ファイル内容をウィジェット上に表示する")
    another.geometry("1400x800")
    another.withdraw()
    frame1=File_Selection(root) 
    frame2=Make_Scrollbar_config(another)
    frame1.Make_Scrollbar_lists()
    frame2.Make_Scrollbar_content()



    References_Link(root)

    frame1.Make_button()

    root.mainloop()

