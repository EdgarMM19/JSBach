# JSBach

Aquest projecte inclou un interpret del llenguatge de programació musical **JSBach**.

L'interpret funciona en Python per tant és un prerequisit igual que ANTLR que s'utilitza com a eina.

La documentació bàsica de aquest llenguatge es pot trobar al projecte [original](https://github.com/jordi-petit/lp-jsbach-2022). Descrivim aqui el us del interpret i les adendes que s'han fet al llenguatge.

## Execució

Primer cal compilar la gramàtica. Si ANTLR es troba instalat només cal fer:
```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor jsbach.g4
```

Podem cridar llavors al interpret amb:

```bash
python3 jsbach.py NOMPROGRAMA.jsb [Funcio parametres] [-NP]
```

On *NOMPROGRAMA.jsb* és el arxiu que volem executar. *Funcio* es la funció per on volem que comenci l'execució (per defecte Main), si aquesta funció té paràmetres numèrics s'han de donar. Si te llistes com paràmetres no es pot començar l'execució desde aquesta funció. Finalment l'opció *-NP* fa que no es reprodueixi música en cas de que s'hagi generat.

## Addendes

### A la crida
Ja s'ha explicat com cridar una funció amb paràmetres i l'ús de _-NP_. Es pot provar amb:
```bash
python3 jsbach.py test-crida.jsb Euclides 15 6
```

### Rück

S'ha fet una extensió per tal que els procediments ja no ho siguin, ara són funcions!

Mijançant la comanda *rück* (*return* en alemany, no ruc de tonto!) seguida de una expressió fem la funció en la que ens trobem acabi i retorni aquest valor, que ha de ser un enter. Així podem utilitzar els valors computats per una funció per tal de ajudar-nos en càlculs intermitjos de una expressió facilitant la programació.

Podem trobar tres exemple de funció (una modificació del *gcd*, una funció *max* i un factorial recursiu) a *test-ruck.jsb* i una implementació de Collatz a *test-collatz.jsb*.

### Asignació a elements de vectors

Tot bon llenguatge de programació ha de poder resoldre el problema de les monedes! Per aixó s'ha inclos poder assignar valors a elements de un vector arbitraris. Aixó es fa amb *v[i] <- valor*. Es pot provar una solució del problema de les monededes a *test-monedes.jsb*.