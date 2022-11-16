OBJ = linkedListmain.o linkedListAddAddress.o linkedListLookUpAddress.o linkedListUpdateInList.o linkedListDeleteFromList.o linkedListDisplayList.o linkedListDisplayAliasForLocation.o linkedListSaveToFile.o linkedListQuit.o llCreateList.o lladdAddressNodeToList.o llprintList.o

ipList: $(OBJ)
	gcc -o ipList $(OBJ)
linkedListmain.o: linkedListmain.c linkedListheader.h
	gcc -c linkedListmain.c
linkedListAddAddress.o: linkedListAddAddress.c linkedListheader.h
	gcc -c linkedListAddAddress.c
linkedListLookUpAddress.o: linkedListLookUpAddress.c linkedListheader.h
	gcc -c linkedListLookUpAddress.c
linkedListUpdateInList.o: linkedListUpdateInList.c linkedListheader.h
	gcc -c linkedListUpdateInList.c
linkedListDeleteFromList.o: linkedListDeleteFromList.c linkedListheader.h
	gcc -c linkedListDeleteFromList.c
linkedListDisplayList.o: linkedListDisplayList.c linkedListheader.h
	gcc -c linkedListDisplayList.c
linkedListDisplayAliasForLocation.o: linkedListDisplayAliasForLocation.c linkedListheader.h
	gcc -c linkedListDisplayAliasForLocation.c
linkedListSaveToFile.o: linkedListSaveToFile.c linkedListheader.h
	gcc -c linkedListSaveToFile.c
linkedListQuit.o: linkedListQuit.c linkedListheader.h
	gcc -c linkedListQuit.c
llCreateList.o: llCreateList.c linkedListheader.h
	gcc -c llCreateList.c
lladdAddressNodeToList.o: lladdAddressNodeToList.c linkedListheader.h
	gcc -c lladdAddressNodeToList.c
llprintList.o: llprintList.c linkedListheader.h
	gcc -c llprintList.c

clean:
	rm -rf a.exe
	rm -rf $(OBJ)