import random
import string
import tkinter as tk
from PIL import Image, ImageTk 

root = tk.Tk()
root.title("Speed Typing")
score = 0
highest_score = 0  # Tạo biến để lưu điểm cao nhất
time_left = 60      # Thời gian 1 lần chơi (giây)

# Chức năng chọn từ ngẫu nhiên
def choose_word():
    return ''.join(random.choices(string.ascii_letters, k=5))   # k là số lượng kí tên xuất hiện 1 lần

# Chức năng kiểm tra từ đã nhập và cập nhật điểm
def check_word(event=None):
    global score, time_left, highest_score  # Bao gồm highest_score là biến toàn cục
    if time_left > 0:
        entered_word = entry.get()
        current_word = display_label.cget("text")
        
        if entered_word == current_word:
            display_label.config(text=choose_word())
            result_label.config(text="Correct", fg="green",bg='#CACA0A')
            score += 10             #Nhập đúng điểm +10

            if score > highest_score:
                highest_score = score  # Cập nhật highest_score nếu đạt được điểm cao mới
                hscore_label.config(text=f"Điểm cao nhất: {highest_score}")
                
        else:
            display_label.config(text=choose_word())
            if entered_word == "":
                result_label.config(text="Please enter a word", fg="red",bg='#CACA0A')
            else:
                result_label.config(text="Incorrect, try again", fg="red",bg='#CACA0A')
                score -= 10                     

        entry.delete(0, tk.END)
        score_label.config(text=f"Score: {score}")

time_label=60
def update_time():
    global time_left, timer
    time_left -= 1
    time_label.config(text=f"Time Left: {time_left} seconds")
    if time_left <= 0: 
        print(time_label)              # Nếu thời gian hết
        time_left =0
        timer=False             # Dừng tiếng báo

    if time_left == 0:
        root.after_cancel(timer)
        check_button.config(text="Time's up!", state=tk.DISABLED)
    else:
        timer = root.after(1000, update_time)

def reset_game(): # Reset game
    global score, time_left
    score = 0       #reset điểm
    time_left = 60 #reset thời gian
    score_label.config(text=f"Score: {score}")
    time_label.config(text=f"Time Left: {time_left} seconds")
    display_label.config(text=choose_word())
    result_label.config(text="")
    check_button.config(text="Kiểm tra", state=tk.NORMAL)
    update_time()

# Tải hình ảnh
background_image = Image.open ("DƯỜNG DẪN ẢNH.jpg")  # Thay thế bằng đường dẫn file ảnh của bạn
window_width, window_height = 800, 500
background_image = background_image.resize((window_width, window_height))
background_photo = ImageTk.PhotoImage(background_image)
image_path = "DƯỜNG DẪN ẢNH.jpg"  # Đặt đường dẫn tới hình ảnh của bạn. Còn không thì để trống 

if image_path.strip() == "":
    # Nếu đường dẫn trống, tạo màu nền mặc định (màu xanh)
    window_width, window_height = 800, 500
    background_photo = tk.PhotoImage(width=window_width, height=window_height)
else:
    try:
        # Tải hình ảnh nếu có đường dẫn
        background_image = Image.open(image_path)
        window_width, window_height = 800, 500
        background_image = background_image.resize((window_width, window_height))
        background_photo = ImageTk.PhotoImage(background_image)
    except FileNotFoundError:
        # Nếu không tìm thấy tệp hình ảnh, sử dụng màu nền mặc định (màu xanh)
        window_width, window_height = 800, 500
        background_photo = tk.PhotoImage(width=window_width, height=window_height)

# Tạo Canvas để đặt ảnh nền
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#00FFFF") # Thay đổi màu bằng tên hoặc dùng mã màu HEX CODE
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Đặt ảnh nền vào Canvas ở phía dưới
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Hiển thị từ random
display_label = tk.Label(root, text=choose_word(), font=("Times New Roman", 40), justify='center',bg='#F1F117', fg='#0750F6')
display_label.pack(padx=20, pady=(80, 20), anchor='center')

# Ô nhập dữ liệu
entry = tk.Entry(root, width=30, font=("Times New Roman", 20))
entry.pack(padx=20, pady=10, anchor='center')
entry.bind("<Return>", check_word) 

# Ô kiểm tra tính chính xác
check_button = tk.Button(root, text="Check", command=check_word, font=("Times New Roman", 30),bg='#BBF3BB',fg='#6808DA')
check_button.pack(padx=20, pady=10, anchor='center')

result_label = tk.Label(root, text="", font=("Times New Roman", 25)) # 
result_label.pack(padx=20, pady=10, anchor='center') 

# Công cụ hiển thị thời gian và điểm
score_label = tk.Label(root, text=f"Score: {score}", font=("Times New Roman", 20),bg='#52F86E',fg='#E8230E')
score_label.pack(padx=20, pady=10, anchor='center')

time_label = tk.Label(root, text=f"Time Left: {time_left} seconds", font=("Times New Roman", 20),bg='#006D77', fg='#EDF6F9')
time_label.pack(padx=20, pady=10, anchor='center')

# Ký tên 
name_label = tk.Label(root, text="Đặng Minh Nhựt", font=("Times New Roman", 10),bg='#000000',fg='#FFFFFF')
name_label.place(x=10, y=10)

# Tạo Label để hiển thị điểm cao nhất
hscore_label = tk.Label(root, text=f"Highest point: {highest_score}", font=("Times New Roman", 20),bg='#52F86E',fg='#E8230E')
hscore_label.place(x=570, y=10)  # Đặt vị trí hiển thị của điểm cao nhất

# Thêm nút "Chơi lại" và gán chức năng reset_game cho nó
play_again_button = tk.Button(root, text="Reset", command=reset_game, font=("Times New Roman", 20),bg='#0A4B89', fg='#E9F31B')
play_again_button.place(x=20, y=200)

# Begin the countdown
update_time()

root.geometry("800x500")
root.mainloop()