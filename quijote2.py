
EL CUENTO DE NUNCA ACABAR
—«Sucedió —dijo Sancho— que el pastor puso por obra su determinación y, antecogiendo sus cabras, se encaminó por los campos de Estremadura, para pasarse a los reinos de Portugal. La Torralba, que lo supo, se fue tras él y seguíale a pie y descalza desde lejos, con un bordón en la mano y con unas alforjas al cuello, donde llevaba, según es fama, un pedazo de espejo y otro de un peine y no sé qué botecillo de mudas para la cara; mas llevase lo que llevase, que yo no me quiero meter ahora en averiguallo, solo diré que dicen que el pastor llegó con su ganado a pasar el río Guadiana, y en aquella sazón iba crecido y casi fuera de madre, y por la parte que llegó no había barca ni barco, ni quien le pasase a él ni a su ganado de la otra parte, de lo que se congojó mucho porque veía que la Torralba venía ya muy cerca y le había de dar mucha pesadumbre con sus ruegos y lágrimas; mas tanto anduvo mirando, que vio un pescador que tenía junto a sí un barco, tan pequeño, que solamente podían caber en él una persona y una cabra; y, con todo esto, le habló y concertó con él que le pasase a él y a trecientas cabras que llevaba. Entró el pescador en el barco y pasó una cabra; volvió y pasó otra; tornó a volver y tornó a pasar otra.» Tenga vuestra merced cuenta en las cabras que el pescador va pasando, porque si se pierde una de la memoria, se acabará el cuento, y no será posible contar más palabra dél. «Sigo, pues, y digo que el desembarcadero de la otra parte estaba lleno de cieno y resbaloso, y tardaba el pescador mucho tiempo en ir y volver. Con todo esto, volvió por otra cabra, y otra, y otra...»
—Haz cuenta que las pasó todas —dijo don Quijote—, no andes yendo y viniendo desa manera, que no acabarás de pasarlas en un año.
—¿Cuántas han pasado hasta agora? —dijo Sancho.
—¿Yo qué diablos sé? —respondió don Quijote.
—He ahí lo que yo dije: que tuviese buena cuenta. Pues por Dios que se ha acabado el cuento, que no hay pasar adelante.
—¿Cómo puede ser eso? —respondió don Quijote—. ¿Tan de esencia de la historia es saber las cabras que han pasado por estenso, que si se yerra una del número no puedes seguir adelante con la historia?
—No, señor, en ninguna manera —respondió Sancho—; porque así como yo pregunté a vuestra merced que me dijese cuántas cabras habían pasado, y me respondió que no sabía, en aquel mesmo instante se me fue a mí de la memoria cuanto me quedaba por decir, y a fe que era de mucha virtud y contento.
—¿De modo —dijo don Quijote— que ya la historia es acabada?
—Tan acabada es como mi madre —dijo Sancho. 


pathquijote='file/quijote1.txt'
def wordsrepeat(file):

    with open(file,'r', encoding='utf8') as f:

        content = f.read()

        words = content.split()

        tmp = {}

        for w in words:

            if w in tmp:

                tmp[w] +=1

            else:

                tmp[w] = 1

        print(tmp)

        minimo = min(tmp, key=tmp.get)

        c_minimo = tmp[minimo]

        maximo = max(tmp, key=tmp.get)

        c_maximo = tmp[maximo]

    return minimo, maximo,c_minimo,c_maximow_min,
w_max, c_min, c_max = wordsrepeat(pathquijote)


print(f'la palabra que menos se repite es "{w_min}" con {c_min} repeticiones, la palabra que mas se repite es "{w_max}" con {c_max} repeticiones')



