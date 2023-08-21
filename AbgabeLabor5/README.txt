Um einen Assembler Code in Hex Code übersetzen zu lassen müssen Sie:
 - die Datei mit dem Assembler Code im Ordner 'code_examples' ablegen.
 - ein Terminal im Ordner in dem sich die Datei 'assembler.py' befindet öffnen
 - python3 installiert haben
 - dann führen Sie im Terminal den Befehl 'python3 assembler.py <ihrDateiNameMitDateiendung>' aus
 - wir empfehlen als Beispielprogramm die Datei 'exampleFinal.txt', sie benutzt alle Befehle
 - im gleichen Ordner befindet sich nun Ihr assembliertes Ergebnis in der Datei 'code_assembled_to_hex'
 - der Assembler assembliert für unsere eigene CPU die sich in von der vorgegeben unterscheidet,
   der Unterschied der beim Assembler Code schreiben beachtet werden muss ist dass unser BEQ eine eigene
   Subtraktion ausführt, es müssen also vorher die beiden Zahlen die verglichen werden sollen 
   in den Registern A und B vorliegen. Es kann deswegen leider nicht mit anderen Operationen wie AND, 
   OR oder ADD verglichen werden
 - Um den assemblierten Code auszuführen, öffnen Sie unsere CPU in Logisim Evolution und laden 
   Sie den assemblierten Code in den Programmspeicher