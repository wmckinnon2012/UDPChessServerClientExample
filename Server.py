import tkinter as tk
from PIL import Image, ImageTk
import threading

import socket




class ChessBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Board")
        self.geometry("800x800")
        self.boardState = {}
        self.create_chessboard()
        img = self.place_image(0, 1, "Chess_ndt60.png")  # Black Knight
        img = self.place_image(0, 6, "Chess_ndt60.png")  # Black Knight
        img = self.place_image(0, 2, "Chess_bdt60.png")  # Black Bishop
        img = self.place_image(0, 5, "Chess_bdt60.png")  # Black Bishop
        img = self.place_image(0, 3, "Chess_qdt60.png")  # Black Queen
        img = self.place_image(0, 4, "Chess_kdt60.png")  # Black King
        img = self.place_image(0, 0, "Chess_rdt60.png")  # Black Rook
        img = self.place_image(0, 7, "Chess_rdt60.png")  # Black Rook
        img = self.place_image(7, 0, "Chess_rlt60.png")  # White Rook
        img = self.place_image(7, 7, "Chess_rlt60.png")  # White Rook
        img = self.place_image(7, 6, "Chess_nlt60.png")  # White Knight
        img = self.place_image(7, 1, "Chess_nlt60.png")  # White Knight
        img = self.place_image(7, 2, "Chess_blt60.png")  # White Bishop
        img = self.place_image(7, 5, "Chess_blt60.png")  # White Bishop
        img = self.place_image(7, 4, "Chess_qlt60.png")  # White Queen
        img = self.place_image(7, 3, "Chess_klt60.png")  # White King

        img = self.place_image(1, 0, "Chess_pdt60.png")  # Replace with the path to your image
        img = self.place_image(1, 1, "Chess_pdt60.png")  # Replace with the path to your image
        img = self.place_image(1, 2, "Chess_pdt60.png")  # Replace with the path to your image
        img = self.place_image(1, 3, "Chess_pdt60.png")  # Replace with the path to your image
        img = self.place_image(1, 4, "Chess_pdt60.png")  # Replace with the path to your image
        img = self.place_image(1, 5, "Chess_pdt60.png")  # Replace with the path to your image
        img = self.place_image(1, 6, "Chess_pdt60.png")  # Replace with the path to your image
        img = self.place_image(1, 7, "Chess_pdt60.png")  # Replace with the path to your image
        img = self.place_image(6, 0, "Chess_plt60.png")  # Replace with the path to your image
        img = self.place_image(6, 1, "Chess_plt60.png")  # Replace with the path to your image
        img = self.place_image(6, 2, "Chess_plt60.png")  # Replace with the path to your image
        img = self.place_image(6, 3, "Chess_plt60.png")  # Replace with the path to your image
        img = self.place_image(6, 4, "Chess_plt60.png")  # Replace with the path to your image
        img = self.place_image(6, 5, "Chess_plt60.png")  # Replace with the path to your image
        img = self.place_image(6, 6, "Chess_plt60.png")  # Replace with the path to your image
        img = self.place_image(6, 7, "Chess_plt60.png")  # Replace with the path to your image

        self.move_piece(1,3,5,5)
        #self.move_piece(1,1,2,2)

    def create_chessboard(self):
        dark_color = "#8c4510"  # Dark squares color
        light_color = "#ffce9e"  # Light squares color

        self.squares = [[None] * 8 for _ in range(8)]

        for row in range(8):
            for col in range(8):
                color = dark_color if (row + col) % 2 == 0 else light_color
                square = tk.Canvas(self, width=100, height=100, bg=color, highlightthickness=0)
                square.grid(row=row, column=col)
                self.squares[row][col] = square
                self.boardState[row,col] = 'empty'
        
        self.squares[0][0].create_text(15, 50, text="1", fill="black", font=('Helvetica 25 bold'))
        self.squares[0][0].create_text(50, 15, text="A", fill="black", font=('Helvetica 25 bold'))
        self.squares[0][1].create_text(50, 15, text="B", fill="black", font=('Helvetica 25 bold'))
        self.squares[0][2].create_text(50, 15, text="C", fill="black", font=('Helvetica 25 bold'))
        self.squares[0][3].create_text(50, 15, text="D", fill="black", font=('Helvetica 25 bold'))
        self.squares[0][4].create_text(50, 15, text="E", fill="black", font=('Helvetica 25 bold'))
        self.squares[0][5].create_text(50, 15, text="F", fill="black", font=('Helvetica 25 bold'))
        self.squares[0][6].create_text(50, 15, text="G", fill="black", font=('Helvetica 25 bold'))
        self.squares[0][7].create_text(50, 15, text="H", fill="black", font=('Helvetica 25 bold'))
        self.squares[1][0].create_text(15, 50, text="2", fill="black", font=('Helvetica 25 bold'))
        self.squares[2][0].create_text(15, 50, text="3", fill="black", font=('Helvetica 25 bold'))
        self.squares[3][0].create_text(15, 50, text="4", fill="black", font=('Helvetica 25 bold'))
        self.squares[4][0].create_text(15, 50, text="5", fill="black", font=('Helvetica 25 bold'))
        self.squares[5][0].create_text(15, 50, text="6", fill="black", font=('Helvetica 25 bold'))
        self.squares[6][0].create_text(15, 50, text="7", fill="black", font=('Helvetica 25 bold'))
        self.squares[7][0].create_text(15, 50, text="8", fill="black", font=('Helvetica 25 bold'))

    def place_image(self, row, col, image_path):
        if 0 <= row < 8 and 0 <= col < 8:
            square = self.squares[row][col]
            if square:
                pil_image = Image.open(image_path)
                tk_image = ImageTk.PhotoImage(pil_image)
                square.create_image(50, 50, image=tk_image)

                square.image = tk_image  # Keep a reference to prevent garbage collection
                self.boardState[row,col] = image_path

    def remove_image(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            square = self.squares[row][col]
            if square:
                del square.image  # Keep a reference to prevent garbage collection
                self.boardState[row,col] = 'empty'

    def validate_move(self,row,col,row2,col2):
        try:
            img = self.boardState[row,col]
        except:
            return False
        #DO NOT CAPTURE YOUR OWN PIECES CHECK"
        if img == "Chess_pdt60.png" or img == "Chess_rdt60.png" or img == "Chess_bdt60.png" or img == "Chess_kdt60.png" or img == "Chess_qdt60.png" or img == "Chess_ndt60.png":
            img2 = self.boardState[row2,col2]
            if img2 == "Chess_pdt60.png" or img2 == "Chess_rdt60.png" or img2 == "Chess_bdt60.png" or img2 == "Chess_kdt60.png" or img2 == "Chess_qdt60.png" or img2 == "Chess_ndt60.png":
                print("tried to capture Own piece")
                return False
        if img == "Chess_plt60.png" or img == "Chess_rlt60.png" or img == "Chess_blt60.png" or img == "Chess_klt60.png" or img == "Chess_qlt60.png" or img == "Chess_nlt60.png":
            img2 = self.boardState[row2,col2]
            if img2 == "Chess_plt60.png" or img2 == "Chess_rlt60.png" or img2 == "Chess_blt60.png" or img2 == "Chess_klt60.png" or img2 == "Chess_qlt60.png" or img2 == "Chess_nlt60.png":
                print("tried to capture Own piece")
                return False
        print(img,img2)
        ruleFailed = ''
        #Pawn Block#
        if(img == 'Chess_pdt60.png' or img == 'Chess_plt60.png'):
            if(abs(row - row2) == 1 and col == col2 and self.boardState[row2,col2] == 'empty'):
                return True
            else:
                ruleFailed = "Pawn Move exceed row Change Limit"
            if(row == 1 and abs(row-row2) == 2 and self.boardState[row2,col2] == 'empty'):
                return True
            else:
                ruleFailed = "Tried double move not from starting row or into a object"
            if(row == 6 and abs(row-row2) == 2 and self.boardState[row2,col2] == 'empty'):
                return True
            else:
                ruleFailed = "Tried double move not from starting row or into a object"
            if(abs(row - row2) == 1 and abs(col - col2) == 1 and self.boardState[row2,col2] != 'empty'):
                return True
            else:
                ruleFailed = "Tried to do pawn Capture move on non valid object"
        #ROOK BLOCK#
        if(img == 'Chess_rdt60.png' or img == 'Chess_rlt60.png'):
            if(row == row2 and col != col2):
                if(col < col2): 
                    numbers_between = list(range(col + 1, col2))
                if(col2 < col):
                    numbers_between = list(range(col2 + 1, col))
                for num in numbers_between:
                    if self.boardState[row,num] == 'empty':
                        print(row,num)
                    else:
                        print ("Rook tried to move through a piece at",row,num)
                        return False
                return True
            else:
               ruleFailed = "Rook tried to move non straight line"
            if(col == col2 and row != row2):
                if(row < row2):
                    numbers_between = list(range(row + 1, row2))
                if(row2 < row):
                    numbers_between = list(range(row2 + 1, row))
                print(row,row2,numbers_between)
                for num in numbers_between:
                    if self.boardState[num,col] == 'empty':
                        print(col,num)
                    else:
                        print ("Rook tried to move through a piece at",col,num)
                        return False
                return True
            else:
               ruleFailed = "Rook tried to move non straight line"
        #Knight Block
        if(img == 'Chess_ndt60.png' or img == 'Chess_nlt60.png'):
            if(abs(row - row2) == 2 and abs(col - col2) == 1):
               return True
            else:
                ruleFailed = "Knight tried to move outside allowed movement"
            if(abs(col - col2) == 2 and abs(row - row2) == 1):
               return True
            else:
                ruleFailed = "Knight tried to move outside allowed movement"
                
        #Bishop Block
        if(img == 'Chess_bdt60.png' or img == 'Chess_blt60.png'):
            if(abs(row - row2) == abs(col - col2)):
                if(row < row2):
                    row_range = list(range(row + 1, row2))
                if(row2 < row):
                    row_range = list(range(row2 + 1, row))
                if(col < col2):
                    print("HERE")
                    col_range = list(range(col + 1, col2))
                if(col2 < col):
                    col_range = list(range(col2 + 1, col))
                    print(col_range)
                i = 0
                print(col_range,row_range)
                while i < len(col_range):
                    if(self.boardState[row_range[i],col_range[i]] == 'empty'):
                       print(row_range[i],col_range[i])
                    else:
                        print("Tried to move bishop through object puked")
                        return False
                    i = i + 1
                return True
            else:
                ruleFailed = "Bishop Tried non diagonal movement"
        #Queen Block
        if(img == 'Chess_qdt60.png' or img == 'Chess_qlt60.png'):
            if(abs(row - row2) == abs(col - col2)):
                if(row < row2):
                    row_range = list(range(row + 1, row2))
                if(row2 < row):
                    row_range = list(range(row2 + 1, row))
                if(col < col2):
                    print("HERE")
                    col_range = list(range(col + 1, col2))
                if(col2 < col):
                    col_range = list(range(col2 + 1, col))
                    print(col_range)
                i = 0
                print(col_range,row_range)
                while i < len(col_range):
                    if(self.boardState[row_range[i],col_range[i]] == 'empty'):
                       print(row_range[i],col_range[i])
                    else:
                        print("Tried to move Queen through object puked")
                        return False
                    i = i + 1
                return True
            else:
                ruleFailed = "Queen Tried non diagonal movement"
            
            if(row == row2 and col != col2):
                if(col < col2): 
                    numbers_between = list(range(col + 1, col2))
                if(col2 < col):
                    numbers_between = list(range(col2 + 1, col))
                for num in numbers_between:
                    if self.boardState[row,num] == 'empty':
                        print(row,num)
                    else:
                        print ("Queen tried to move through a piece at",row,num)
                        return False
                return True
            else:
               ruleFailed = "Queen tried to move non valid"
            if(col == col2 and row != row2):
                if(row < row2):
                    numbers_between = list(range(row + 1, row2))
                if(row2 < row):
                    numbers_between = list(range(row2 + 1, row))
                print(row,row2,numbers_between)
                for num in numbers_between:
                    if self.boardState[num,col] == 'empty':
                        print(col,num)
                    else:
                        print ("Queen tried to move through a piece at",col,num)
                        return False
                return True
            else:
               ruleFailed = "Queen tried to move non valid"
        #King Block
        if(img == 'Chess_kdt60.png' or img == 'Chess_klt60.png'):
            if(abs(row - row2) < 2 and abs(col - col2 < 2)):
               return True
            else:
                ruleFailed = "King tried to move more then one space"
        print("Ivalid Move Attempted " + ruleFailed)
        return False
    def translate_command(self,dataString):
        try:
            locCol = int(dataString[1]) - 1
        except:
            print('failed to cast command')
        try:
            locCol2 = int(dataString[3]) - 1
        except:
            print('failed to cast command')
        if(dataString[0] == 'a' or dataString[0] == 'A'):
           locRow = 0
        if(dataString[0] == 'b' or dataString[0] == 'B'):
           locRow = 1
        if(dataString[0] == 'c' or dataString[0] == 'C'):
           locRow = 2
        if(dataString[0] == 'd' or dataString[0] == 'D'):
           locRow = 3
        if(dataString[0] == 'e' or dataString[0] == 'E'):
           locRow = 4
        if(dataString[0] == 'f' or dataString[0] == 'F'):
           locRow = 5
        if (dataString[0] == 'g' or dataString[0] == 'G'):
            locRow = 6
        if (dataString[0] == 'h' or dataString[0] == 'H'):
            locRow = 7
        if dataString[2] == 'a' or dataString[2] == 'A':
            locRow2 = 0
        if dataString[2] == 'b' or dataString[2] == 'B':
            locRow2 = 1
        if dataString[2] == 'c' or dataString[2] == 'C':
            locRow2 = 2
        if dataString[2] == 'd' or dataString[2] == 'D':
            locRow2 = 3
        if dataString[2] == 'e' or dataString[2] == 'E':
            locRow2 = 4
        if dataString[2] == 'f' or dataString[2] == 'F':
            locRow2 = 5
        if dataString[2] == 'g' or dataString[2] == 'G':
            locRow2 = 6
        if dataString[2] == 'h' or dataString[2] == 'H':
            locRow2 = 7

        print(locCol,locRow,locCol2,locRow2)
        self.move_piece(locCol,locRow,locCol2,locRow2)
        
    def move_piece(self,row,col,row2,col2):
        if self.validate_move(row,col,row2,col2):
            img = self.boardState[row,col]
            self.remove_image(row,col)
            self.place_image(row2,col2,img)

    def udp_server(self):
        # Create a UDP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind the socket to a specific address and port
        server_address = ('127.0.0.1', 12345)  # Change the IP and port as needed
        server_socket.bind(server_address)

        print(f"UDP server is listening on {server_address}")

        try:
            while True:
                # Receive data from the client
                data, client_address = server_socket.recvfrom(2048)
                
                # Process the received data
                print(f"Received data from {client_address}: {data.decode('utf-8')}")
                # Send a response back to the client
                dataInp = data.decode('utf-8')
                print(dataInp)
                self.translate_command(dataInp)
                #self.move_piece(1,1,2,2)

                sendString = ""
                for state in self.boardState:
                    sendString = sendString + str(state) + '§' + str(self.boardState[state]) + '&'
                response = str(sendString)
                server_socket.sendto(response.encode('utf-8'), client_address)

        except KeyboardInterrupt:
            print("Server shutting down.")
        finally:
            # Close the socket when done
            server_socket.close()

    def run(self):
        thread1 = threading.Thread(target=self.udp_server)
        thread2 = threading.Thread(target=self.mainloop)


        #self.udp_server()

        thread1.start()
        self.mainloop()
if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.run()

