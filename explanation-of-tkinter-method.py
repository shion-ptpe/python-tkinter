import tkinter as tk
import webbrowser

# 関数定義ーーーーーーーーーーーーーーーーーーーーーーーーーーー
# フラグの設定
forgetFrame_flag = False
# メソッドの説明
pack_text= "pack は親ウィジェット上にウィジェットを詰め込むメソッド。\n\
[ウィジェット名].pack() で記述する。\n\
今回は\npack1.pack(side=tk.TOP)\n\
pack2.pack(side=tk.TOP)\n\
pack3.pack(side=tk.TOP)\n\
で設定してある。\n\
引数は「side」「expand」「anchor」「fill」「padx」などがある。"
grid_text= "grid は親ウィジェットを２次元的に複数のセルに分割し、\n\
各セルにウィジェットを配置するメソッド。\n\
[ウィジェット名].grid(column=[値], row=[値]) で記述する。\n\
今回は\n\
grid1.grid(column=0, row=0)\n\
grid2.grid(column=1, row=0)\n\
grid3.grid(column=0, row=1)\n\
grid4.grid(column=1, row=1)\n\
grid5.grid(column=0, row=2)\n\
grid6.grid(column=1, row=2)\n\
で設定してある。\n\
「column」は列、「row」は行を表す。\n\
引数は「sticky」「columnspan」「rowspan」「padx」などがある。"
place_text = "place は親ウィジェット上の座標を指定して、その座標にウィジェットを配置するメソッド。\n\
[ウィジェット名].place(x=[値], y=[値]) で記述する。\n\
今回は\n\
button1.place(x=20, y=20)\n\
button2.place(x=65, y=70)\n\
button3.place(x=45, y=155)\n\
で設定してある。\n\
「x」・「y」は座標を表す。\n\
引数は「width」「height」「relx」「rely」などがある。"
# ボタンの設定 (packの説明を詳しく)
def forgetFrame_pack():
    global forgetFrame_flag
    global more_explain_pack
    if forgetFrame_flag:
        more_explain_pack.pack_forget()
        example_grid.pack(side=tk.LEFT)
        example_place.pack(side=tk.LEFT)
        forgetFrame_flag = False
    else:
        example_grid.pack_forget()
        example_place.pack_forget()
        more_explain_pack = tk.Label(example, text=pack_text,justify="left",font=("normal","15"))
        more_explain_pack.pack(fill=tk.X, side=tk.LEFT)
        forgetFrame_flag = True
# ボタンの設定 (gridの説明を詳しく)
def forgetFrame_grid():
    global forgetFrame_flag
    global more_explain_grid
    if forgetFrame_flag:
        more_explain_grid.pack_forget()
        example_pack.pack(side=tk.LEFT)
        example_place.pack(side=tk.LEFT)
        forgetFrame_flag = False
    else:
        example_pack.pack_forget()
        example_place.pack_forget()
        more_explain_grid = tk.Label(example, text=grid_text,justify="left",font=("normal","15"))
        more_explain_grid.pack(fill=tk.X, side=tk.LEFT)
        forgetFrame_flag = True
# ボタンの設定 (placeの説明を詳しく)
def forgetFrame_place():
    global forgetFrame_flag
    global more_explain_place
    if forgetFrame_flag:
        more_explain_place.pack_forget()
        example_pack.pack(side=tk.LEFT)
        example_grid.pack(side=tk.LEFT)
        forgetFrame_flag = False
    else:
        example_pack.pack_forget()
        example_grid.pack_forget()
        more_explain_place = tk.Label(example, text=place_text,justify="left",font=("normal","15"))
        more_explain_place.pack(fill=tk.X, side=tk.LEFT)
        forgetFrame_flag = True

# 座標を取得する関数
def xy_print(event):
    line = 'x:' + str(event.x) + ' ' + 'y:' + str(event.y)  # str・・・引数に指定した数値などのオブジェクトを文字列に変換して取得できる、.x・・・ウィジェット上のx座標、+は文字列の結合
    textbox.delete(0, 20)  # delete・・・文字を削除。第１パラメータはテキストボックス内の削除開始位置。第２パラメータはテキストボックス内の削除終了位置。
    textbox.insert(0, line)  # insert・・・テキストボックスに文字を入力する、第一パラメータは文字をセットする位置、第２パラメータは入力する文字

# 参考文献のリンク作成の関数
def jump_to_link(url):  # urlクリック時の動作を定義
    webbrowser.open_new(url)
def make_link(link_title, Destination):
    link_wid = tk.Button(link,text=link_title, foreground="#346592", activeforeground="#734898",cursor="hand2")
    link_wid.bind("<ButtonPress>", lambda e:jump_to_link(Destination))
    link_wid.pack(side =tk.BOTTOM,anchor=tk.W)



# ウィジェットの配置を始める-------------------------------------------------------------------------------
root = tk.Tk()
root.title("placeを使ったプログラム")
root.geometry("800x600")
# タイトルの設定
title = tk.Frame(root, background="#ffffff", height=50)
title.pack(fill=tk.X, anchor=tk.N, pady=1)
label = tk.Label(title, text="tkinterコマンドの説明", font=("normal","25","bold"),foreground='#000000', background="#ffffff")
label.pack(pady=10)
# pack・grid・placeのざっくりとした説明
explain = tk.LabelFrame(root)
explain.pack(fill=tk.X)

explain_pack = tk.Label(explain, text="pack・・・ある方向に対してどんどんウィジェットを詰め込んでいくイメージ", font=("normal","15"))
explain_pack.pack(anchor=tk.W)
explain_grid = tk.Label(explain, text="grid・・・2次元的に複数のセルに分割", font=("normal","15"))
explain_grid.pack(anchor=tk.W)
explain_place = tk.Label(explain, text="place・・・座標を指定して、その座標にウィジェットを配置する", font=("normal","15"))
explain_place.pack(anchor=tk.W)

# 使い方の説明を記述するためのフレームを作成
example = tk.Frame(root, width=600)
example.pack()
# packの使い方ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
example_pack = tk.LabelFrame(example, text="packの使い方", borderwidth=10, height=330, width=200, padx=25, pady=25,font=("normal","20"))
example_pack.propagate(False)
tk.Label(example_pack, background="#ff0000", height=2, width=17).pack(side=tk.TOP)
tk.Label(example_pack, background="#008000", height=4, width=3).pack(side=tk.TOP)
tk.Label(example_pack, background="#0000ff",height=3, width=12).pack(side=tk.TOP)

button_pack = tk.Button(example_pack, text="packについて詳しく", relief=tk.RAISED, cursor="hand2", command=forgetFrame_pack)
button_pack.place(x=0, y=240)

example_pack.pack(side=tk.LEFT)

# gridの使い方ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
example_grid = tk.LabelFrame(example, text="gridの使い方", borderwidth=10, height=330,width=200,padx=28, pady=25,font=("normal","20"))
example_grid.grid_propagate(False)
# ラベル（図）を書く
tk.Label(example_grid, text="1", foreground="#000000", background="#ff0000", padx=25, pady=30).grid(column=0, row=0)
tk.Label(example_grid, text="2", foreground="#000000", background="#ffa500", padx=25, pady=30).grid(column=1, row=0)
tk.Label(example_grid, text="3", foreground="#000000", background="#ffff00", padx=25, pady=30).grid(column=0, row=1)
tk.Label(example_grid, text="4", foreground="#000000", background="#008000", padx=25, pady=30).grid(column=1, row=1)
tk.Label(example_grid, text="5", foreground="#000000", background="#00ffff", padx=25, pady=30).grid(column=0, row=2)
tk.Label(example_grid, text="6", foreground="#000000", background="#800080", padx=25, pady=30).grid(column=1, row=2)

button_grid2 = tk.Button(example_grid, text="gridについて詳しく", relief=tk.RAISED, cursor="hand2", command=forgetFrame_grid)
button_grid2.place(x=0, y=240)

example_grid.pack(side=tk.LEFT)

# placeの使い方---------------------------------------------
example_place = tk.LabelFrame(example, text="placeの使い方", borderwidth=10, height=330,width=200, padx=3, pady=0,font=("normal","20"))
example_place.propagate(False)
# 座標を表示するウィジェット
textbox = tk.Entry(example_place, width=18)  # Entry・・・テキストボックスを表示
textbox.pack()
canvas = tk.Canvas(example_place, height=230, width=170, bg='white')  # canvas・・・キャンバスを表示
canvas.pack()
canvas.bind('<Motion>', xy_print)  # Motion・・・パーツ内でマウスが動くと起こるイベント。

# ボタンを並べる
button_place1 = tk.Button(canvas, text="button1", relief=tk.RAISED)
button_place1.place(x=20, y=20)  # canvasを基準とした座標を指定
button_place2 = tk.Button(canvas, text="button2", relief=tk.RAISED)
button_place2.place(x=65, y=70)
button_place3 = tk.Button(canvas, text="button3", relief=tk.RAISED)
button_place3.place(x=45, y=155)

button_place = tk.Button(example_place, text="placeについて詳しく", relief=tk.RAISED, cursor="hand2", command=forgetFrame_place)
button_place.place(x=18, y=265)

example_place.pack(side=tk.LEFT)


# 参考文献--------------------------------------------------------------
link = tk.Frame(root)
link.pack(side = tk.LEFT, anchor=tk.S)
link_References = tk.Label(link,text="参考文献")
# ハイパーリンクを作る関数を呼び出す
make_link("tkinter | イメージングソリューション","https://imagingsolution.net/tag/tkinter/")
make_link("Python | OFFICE54","https://office54.net/python/")
make_link("「Tkinterの使い方」の記事一覧 | だえうホームページ","https://daeudaeu.com/category/python/tkinter/tkinter_tutorial/")
make_link("Tkinterの使い方：ウィジェットの配置（pack・grid・place）","https://daeudaeu.com/tkinter_place/#pack-3")
link_References.pack(side =tk.BOTTOM, anchor=tk.W)

# quitボタンを作成
quit_button = tk.Frame(root)
quit_button.pack(side = tk.RIGHT, anchor=tk.S)

button = tk.Button(quit_button, text="Quit", relief=tk.RAISED, cursor="hand2", command=root.destroy)
button.pack(side =tk.BOTTOM, ipadx=5)

root.mainloop()
