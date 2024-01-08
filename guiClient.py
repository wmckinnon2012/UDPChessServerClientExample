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
        self.selectedPiece = [-1,-1]
        self.selectedDesiredMoveSpace = [-1,-1]

        # Bind mouse click to move the image
            
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
    def on_square_click(self, event):
        print(event.widget)
        if(str(event.widget) == ('.!canvas')):
            self.selectedPiece = [0,0]
            return
        row = ((int(str(event.widget).split('s')[1]) -1) // 8)
        col = (int(str(event.widget).split('s')[1]) - 1)
        while (col >= 8):
            col = col - 8
        self.selectedPiece = [row,col]
        row = event.y // 50
        col = event.x // 50
        #print(row,col)
        print(self.selectedPiece)
        
    def on_square_right_click(self, event):
        print(event.widget)
        if(str(event.widget) == ('.!canvas')):
            self.selectedDesiredMoveSpace = [0,0]
            self.convertMessage()
            return
        row = ((int(str(event.widget).split('s')[1]) -1) // 8)
        col = (int(str(event.widget).split('s')[1]) - 1)
        while (col >= 8):
            col = col - 8
        self.selectedDesiredMoveSpace = [row,col]
        row = event.y // 50
        col = event.x // 50
        #print(row,col)
        #print(self.selectedDesiredMoveSpace)
        self.convertMessage()
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
                square.bind("<Button-1>", self.on_square_click)
                square.bind("<Button-3>", self.on_square_right_click)

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
    def convertMessage(self):
        message = ''
        print(self.selectedPiece[1])
        if self.selectedPiece[1] >= 0 and self.selectedPiece[1] <= 7:
            message = message + chr(ord('A') + self.selectedPiece[1])
        message = message + str(self.selectedPiece[0] + 1)
        if self.selectedDesiredMoveSpace[1] >= 0 and self.selectedDesiredMoveSpace[1] <= 7:
            message = message + chr(ord('A') + self.selectedDesiredMoveSpace[1])
        message = message + str(self.selectedDesiredMoveSpace[0] + 1)
        print(message)
        print(self.selectedPiece)
        print(self.selectedDesiredMoveSpace[1])
        self.udp_client(message)
    def udp_client(self,message):
        # Create a UDP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Server address and port
        server_address = ('127.0.0.1', 12345)  # Change to match the server's IP and port

        try:
            # Send data to the server
            #message = "C7D8"
            client_socket.sendto(message.encode('utf-8'), server_address)

            # Receive the response from the server
            data, server_address = client_socket.recvfrom(2048)
            print(f"Received response from {server_address}: {data.decode('utf-8')}")
            localDict = (data.decode().split(':'))
            keyValuePairs = (localDict[0].split('&'))
            for pair in keyValuePairs:
                keyAndValues = pair.split('§')
                try:
                    coordInts = keyAndValues[0].strip('(').strip(' ').strip(')').split(',')
                    print(int(coordInts[0]),int(coordInts[1]), keyAndValues[1])
                    row = int(coordInts[0])
                    col = int(coordInts[1])
                    img = keyAndValues[1]
                    self.remove_image(row,col)

                except:
                    print("Fails on Junk at end of send Ignore this message")
                if(img != "empty"):
                    self.place_image(row,col,img)

                    
            #strippedDict = (localDict[1].strip('}'))
            #print(strippedDict.split()
            #for entry in localDict:
            #    print(entry)


        finally:
            # Close the socket when done
            client_socket.close()

if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.udp_client('C7D8')
