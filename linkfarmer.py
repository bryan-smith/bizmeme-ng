from re import search, findall
from utils.chandata import ChanBoards
from utils.operations import getThreadIdsFromCatalog, getThread, getCommentsFromThreadAsList

board = "pol"

threadsIdList = getThreadIdsFromCatalog(board)
if threadsIdList == None:
    exit()

commentList = []
print(f"Total threads {len(threadsIdList)}")

for counter, threadId in enumerate(threadsIdList):

    thread = getThread(board, threadId)
    if thread != None:

        # commentList += getCommentsFromThreadAsList(thread)

        for c in getCommentsFromThreadAsList(thread):
            comment = c
            comment = comment.replace("<br>", "\n")
            comment = comment.replace("&quot;", "\"")
            comment = comment.replace("&gt;", ">")
            comment = comment.replace("&lt;", "<")
            comment = comment.replace("<wbr>", "")
            comment = comment.replace("<span class=\"quote\">","")
            comment = comment.replace("</span>","")
            comment = comment.replace("&#039;","\'")
            comment = comment.replace("&amp;","&")
            comment = comment.replace("</a>","")
            comment = comment.replace("<a>","")
            comment = comment.replace("\""," ")
            comment = comment.replace(">"," ")

            t = findall(r'(https?://\S+)', comment)
            if len(t) > 0:
                for link in t:
                    print(link)

        # print(f"O {counter}/{len(threadsIdList)}", flush=True)
    
    else:
        pass
        # print(f"X {counter}/{len(threadsIdList)}", flush=True)

for i in commentList: print(i)