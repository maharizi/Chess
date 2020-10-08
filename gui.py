import pickle
from tkinter import *
import math
import pygame
import chess3
from sys import stderr


def function1():
    print("1")
    chessGame = chess3.chessboard()
    # Arrange a board from the beginning
    chessGame.regularBoard()

    chessGame.updateAll()
    chessGame.updateAll()
    chessGame.afterUpdate()
    screenSize = 360, 360
    display = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Chess Game")
    runGame = True
    time = 0
    clock = pygame.time.Clock()
    pieceInHand = None
    mPos = (0, 0)
    mOffset = (0, 0)
    print(chessGame)
    while (runGame):
        mPos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # save game automatically
            with open('SaveGame.pkl', 'wb') as saveGame:
                pickle.dump(chessGame, saveGame)
            # Click on Exit
            if (event.type == pygame.QUIT):
                runGame = False
                pygame.quit()

            # If no yet winner
            if (chessGame.winner == -1):
                # Catch the piece with the mouse
                if (event.type == 5):
                    i1 = chessGame.getPieceAt((int(mPos[0] / 45), int(mPos[1] / 45)))
                    if (i1 and i1.team == chessGame.currentTeam):
                        mOffset = (int(mPos[0] % 45), int(mPos[1] % 45))
                        if (pieceInHand):
                            pieceInHand.canRender = True
                        i1.canRender = False
                        pieceInHand = i1
                        # pieceInHand.update();

            # Leave the piece with the mouse
            if (event.type == 6):
                if (pieceInHand):
                    if (chessGame.move(pieceInHand.pos, (int(mPos[0] / 45), int(mPos[1] / 45)))):
                        print(chessGame)
                        print("Current player: {}".format("black" if chessGame.currentTeam else "white"))
                    pieceInHand.canRender = True
                    pieceInHand = None

        display.fill((0, 0, 0))

        chessGame.renderBG(display)
        if (pieceInHand):
            dPm = pieceInHand
        else:
            dPm = chessGame.getPieceAt((int(mPos[0] / 45), int(mPos[1] / 45)))
        # Coloring possible moves
        if (dPm and dPm.team == chessGame.currentTeam):
            for i in dPm.validMoves:
                cDiff = -100 * ((i[0] + 1 + i[1]) % 2)
                c = (0, 255 + cDiff, 0)
                pAt = chessGame.getPieceAt(i)
                if (pAt):
                    if (pAt.team != dPm.team):
                        c = (255 + cDiff, 0, 0)
                    else:
                        c = (0, 0, 255 + cDiff)
                pygame.draw.rect(display, c, (i[0] * 45, i[1] * 45, 45, 45))

        chessGame.renderPieces(display)
        if (pieceInHand):
            p = pieceInHand
            s = pieceInHand.spritesheet
            display.blit(s[0], (mPos[0] - mOffset[0], mPos[1] - mOffset[1]), (
                (p.spriteIndex[p.team] % 6) * s[1], math.floor(p.spriteIndex[p.team] / 6) * s[1], s[1], s[1]))
        clock.tick(60)
        pygame.display.update()
        time += 0.1


def function2():
    print("2")
    try:
        with open('SaveGame.pkl', 'rb') as loadGame:
            chessGame = pickle.load(loadGame)
            print(chessGame)
            # Arrange a board from the beginning

            chessGame.updateAll()
            chessGame.afterUpdate()
            screenSize = 360, 360
            display = pygame.display.set_mode(screenSize)
            pygame.display.set_caption("Chess Game")
            runGame = True
            time = 0
            clock = pygame.time.Clock()
            pieceInHand = None
            mPos = (0, 0)
            mOffset = (0, 0)
            print(chessGame)
            while (runGame):
                mPos = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    # save game automatically
                    with open('SaveGame.pkl', 'wb') as saveGame:
                        pickle.dump(chessGame, saveGame)
                    # Click on Exit
                    if (event.type == pygame.QUIT):
                        runGame = False
                        pygame.quit()

                    # If no yet winner
                    if (chessGame.winner == -1):
                        # Catch the piece with the mouse
                        if (event.type == 5):
                            i1 = chessGame.getPieceAt((int(mPos[0] / 45), int(mPos[1] / 45)))
                            if (i1 and i1.team == chessGame.currentTeam):
                                mOffset = (int(mPos[0] % 45), int(mPos[1] % 45))
                                if (pieceInHand):
                                    pieceInHand.canRender = True
                                i1.canRender = False
                                pieceInHand = i1
                                # pieceInHand.update();

                    # Leave the piece with the mouse
                    if (event.type == 6):
                        if (pieceInHand):
                            if (chessGame.move(pieceInHand.pos, (int(mPos[0] / 45), int(mPos[1] / 45)))):
                                print(chessGame)
                                print("Current player: {}".format("black" if chessGame.currentTeam else "white"))
                            pieceInHand.canRender = True
                            pieceInHand = None

                display.fill((0, 0, 0))

                chessGame.renderBG(display)
                if (pieceInHand):
                    dPm = pieceInHand
                else:
                    dPm = chessGame.getPieceAt((int(mPos[0] / 45), int(mPos[1] / 45)))
                # Coloring possible moves
                if (dPm and dPm.team == chessGame.currentTeam):
                    for i in dPm.validMoves:
                        cDiff = -100 * ((i[0] + 1 + i[1]) % 2)
                        c = (0, 255 + cDiff, 0)
                        pAt = chessGame.getPieceAt(i)
                        if (pAt):
                            if (pAt.team != dPm.team):
                                c = (255 + cDiff, 0, 0)
                            else:
                                c = (0, 0, 255 + cDiff)
                        pygame.draw.rect(display, c, (i[0] * 45, i[1] * 45, 45, 45))

                chessGame.renderPieces(display)
                if (pieceInHand):
                    p = pieceInHand
                    s = pieceInHand.spritesheet
                    display.blit(s[0], (mPos[0] - mOffset[0], mPos[1] - mOffset[1]), (
                        (p.spriteIndex[p.team] % 6) * s[1], math.floor(p.spriteIndex[p.team] / 6) * s[1], s[1], s[1]))
                clock.tick(60)
                pygame.display.update()
                time += 0.1
    except:
        print('No saved game data found !')


def function3():
    print("3")
    countB = 0
    countW = 0
    print(file=stderr)
    grades_file = open('Grades.txt', 'r')
    for line in grades_file:
        if line == 'BLACK wins!\n':
            countB = countB + 1
        if line == 'WHITE wins!\n':
            countW = countW + 1
    grades_file.close()
    print("BLACK: ", countB)
    print("WHITE: ", countW)

    root3 = Tk()
    root3.geometry("400x100")
    # title of the window
    root3.title("Grades")

    list = [(countB, 'שחור'), (countW, 'לבן')]

    height = 2
    width = 2
    # code for creating table
    for i in range(height):  # Rows
        for j in range(width):  # Columns
            b = Entry(root3, width=17, fg='blue', font=('Arial', 16, 'bold'))
            b.grid(row=i, column=j)
            b.insert(INSERT, list[i][j])

    root3.mainloop()


def function4():
    print("4")
    root4 = Tk()
    root4.geometry("400x600")
    # title of the window
    root4.title("Rules")
    # titel in the window
    label = Label(root4, text=": כללי המשחק", bg="blue")
    label.place(x=150, y=50)
    # text in group configuration
    text = Text(root4)
    text.tag_configure('tag-right', justify='right')

    text.insert(INSERT,
                'בשחמט לכל כלי דרך תנועה שונה. לעולם אי אפשר לנוע לתוך משבצת שנמצא בה כלי מהצבע של המשחק, או לעבור מעל כלי כזה (מלבד הפרש) ', 'tag-right')
    text.place(x=0, y=100, width=397)
    text.insert(INSERT, '\n')
    text.insert(INSERT,
                'בנוסף, ישנה אפשרות של "הכאה": להסיר כלי של היריב מהלוח. הכאה מתבצעת לרוב כדרך התנועה (מלבד הרגלי) .הכלי נע תמיד למשבצת בה היה כלי היריב ', 'tag-right')
    text.insert(INSERT, '\n')
    text.insert(INSERT,
                'הכלים בעלי תנועה "ארוכה" (מלכה, צריח ורץ) יכולים לנוע כרצונם כל עוד אין בדרך כלי מצבעם, או כלי מה צבע השני שאז עליהם לעצור לפניו, או להכות אותו ', 'tag-right')
    text.insert(INSERT, '\n')
    text.insert(INSERT, '.מלך: המלך יכול לנוע ערוגה אחת לכל כיוון ', 'tag-right')
    text.tag_add('1', "4.0", "4.40")
    text.tag_config('1', background="yellow")
    text.insert(INSERT, '\n')
    text.insert(INSERT, 'מלכה: המלכה יכולה לנוע מספר בלתי מוגבל של משבצות .לכל כיוון ', 'tag-right')
    text.tag_add('2', "5.0", "5.60")
    text.tag_config('2', background="blue")
    text.insert(INSERT, '\n')
    text.insert(INSERT, ' ,צריח: הצריח יכול לנוע מספר בלתי מוגבל של משבצות בטורים ובשורות', 'tag-right')
    text.tag_add('3', "6.0", "6.70")
    text.tag_config('3', background="Brown")
    text.insert(INSERT, '\n')
    text.insert(INSERT,
                '.פרש: הפרש יכול לנוע שתי ערוגות בטורים או בשורות  ואז ערוגה נוספת בניצב לכיוון בו החל ללכת, כך     .מתקבלת צורת האות ר', 'tag-right')
    text.tag_add('4', "7.0", "7.120")
    text.tag_config('4', background="Purple")
    text.insert(INSERT, '\n')
    text.insert(INSERT,
                ' לפרש מותר לדלג מעל כלים אחרים משני הצבעים במהלך תנועתו, אך הערוגה אליה הוא מגיע בסוף התנועה חייבת .להיות פנויה או מאויישת על ידי כלי מהצבע הנגדי', 'tag-right')
    text.tag_add('4', "8.0", "8.150")
    text.tag_config('4', background="Purple")
    text.insert(INSERT, '\n')
    text.insert(INSERT, 'רץ: הרץ יכול לנוע מספר בלתי מוגבל של משבצות,באלכסונים', 'tag-right')
    text.tag_add('5', "9.0", "9.70")
    text.tag_config('5', background="Green")
    text.insert(INSERT, '\n')
    text.insert(INSERT,
                'רגלי: הרגלי יכול לנוע רק קדימה ולהכות כלי אחר     באלכסון קדימה. במסע הראשון של כל רגלי ניתנת לו    .הזכות לצעוד שני צעדים קדימה', 'tag-right')
    text.tag_add('6', "10.0", "10.130")
    text.tag_config('6', background="Red")
    text.insert(INSERT, '\n')
    text.insert(INSERT,
                ' כאשר מגיע הרגלי לשורה האחרונה של הלוח, מתרחש מצב הקרוי "הכתרה". הרגלי הופך לכלי אחר, על פי בחירת  השחקן, באותו הצבע. ניתן להפוך את הרגלי לכל כלי    .פרט למלך', 'tag-right')
    text.tag_add('6', "11.0", "11.160")
    text.tag_config('6', background="Red")
    text.insert(INSERT, '\n')
    text.insert(INSERT, '\n')
    text.insert(INSERT, '.המטרה: להפיל את המלך של היריב', 'tag-right')
    text.tag_add('7', "13.0", "13.70")
    text.tag_config('7', background="Black", foreground="white")
    text.insert(INSERT, '\n')

    root4.mainloop()


root = Tk()
root.geometry("400x400")

# title of the window
root.title("Menu")
newGame = Button(root, text="התחל משחק חדש", bg="blue", fg="white", command=function1)
newGame.place(x=100, y=100, width=200, height=40)
continuGame = Button(root, text="המשך משחק קודם", bg="blue", fg="white", command=function2)
continuGame.place(x=100, y=150, width=200, height=40)
Grades = Button(root, text="ציונים", bg="blue", fg="white", command=function3)
Grades.place(x=100, y=200, width=200, height=40)
Instructions = Button(root, text="כללי המשחק", bg="blue", fg="white", command=function4)
Instructions.place(x=100, y=250, width=200, height=40)

root.mainloop()

