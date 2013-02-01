# Files inlezen en wegschrijven


Een veel voorkomende toepassing van computerprogramma’s is het inlezen en verwerken 
van grote data bestanden. We zullen vandaag een korte toepassing bekijken hiervan. 
Jullie hebben gisteren al even geoefend met het inlezen een doorlopen van files, 
maar hier nog een paar korte voorbeelden. Lees zonodig ook de online documentatie door.

1) openen file, doorlopen van elke regel (en print deze) en sluit de file weer:

          input_filehandle = open(’inputfile.txt’, ’r’) 
          for line in input_filehandle:
              print line 
          input_filehandle.close()

Toegang tot de verschillende parameters in de regel (een string) krijg je door de 
regel in stukken te ’knippen’, bijvoorbeeld met behulp van het `split` commando. 
Het commando `elementen = line.split()` levert een list op met elementen die de 
losse stukken bevatten. Deze elementen kan je aan variabelen toekennen en daarop 
weer afzonderlijke bewerkingen uitvoeren.

2) inlezen en uitschrijven file:

       input_filehandle = open(’inputfile.txt’, ’r’) 
       output_filehandle = open(’outputfile.txt’, ’w’) 
       for line in input_filehandle:
           newline = line + " XXXX"
           output_filehandle.write(newline) 
       input_filehandle.close() 
       output_filehandle.close()
