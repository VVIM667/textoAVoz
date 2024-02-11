import pyttsx3
import os

def text_to_speech_and_save(text: str, file_name: str = "audio.mp3", rate: int = 150) -> None:
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.save_to_file(text, "audio.wav")
    engine.runAndWait()

# Ejemplo de uso
texto = '''1 Naces

2 Tlalpan

3 No mames y que hay ahí?

4 Ni Walmart, puras pinches avenidas

5 Diario atropellan a pendejos que se cruzan por abajo de los puentes

6 Entras a la secu y descubres el delicioso manjar que es comer comida chatarra

7 Chicharrones preparados, chamoyadas y tus favoritas: las sopas Maruchan

8 Te maman tanto a pesar de que dicen que son puro plástico

9 Te digo que son ligas we, dross lo dijo en un top. 

10 Tu favorita era la de camarón con habanero

11 Hija de su espinoza madre están pasadisimas de verga esas madres

12 Igual no las comes mucho porque sientes que te empezarás a hartar de ellas

13 Pero en fin, ser sommelier de la Anemia no te deja muchos amigos

14 Tenías compas que jugaban contigo al Clash y todo

15 Pero ninguno pondría en riesgo el nudo del globo por ti y eso lo sabes

16 La vida de un crítico es dura en muchos aspectos

17 Un día hay mucha conmoción porque dicen que llegó un nuevo alumno

18 Nadie sabe quién es ni a dónde va a ir

19 A ti te vale verga, andabas dibujando un Broly cholo cuando derrepente escuchas un putero de ruido

20 Volteas y ves entrar al salón a una china

21 Traía los ojos cerrados como si estuviera haciendo mucho aire o mucho sol

22 No we, así los tienen ellos

23 A no mames 

24 Cuando llega el profesor de historia la presenta

25 Se llamaba Toru

26 Es japonesa

27 Le dice a Toru que se pare y se presente pero no habla español 

28 Viéndola ya con atención no está tan culera

29 Está blanquita y con el cubre bocas se ve UwU

30 De todos modos se ve que es bien mamona porque como que anda siscada de que le digan china

31 Empieza la clase de historia, hoy tocaba ver a Benito Juárez

32 Desde que tú maestro se llama Itzcoatl sabes que ya valió verga

33 Una hora completa de pura grilla morensita

34 Lo mero ricote pa

35 De repente volteas a ver a Toru y está mirando su mesa vacía, como si estuviera pendeja

36 Suena la campana del receso y todos salen en verguiza

37 Tu te quedas porque tienes que asegurarte de que no te cambien tu silla por la que tiene dibujado un pito

38 También se queda Toru

39 A chinga, si estará pendeja?

40 En eso ves que saca un tupper y lo abre

41 Alaberga huele bien chido

42 Son fideos

43 Así como la Maruchan

44 Pero con chingaderas de colores y carne

45 Derrepente saca dos palitos y se lo empieza a comer así

46 Te empieza a rugir la pinche tripa y ves de reojo tu pinche chanwis de huevo aplastado

47 Te tragas el orgullo y te sientas al lado de ella

48 Me das?

49 Se te queda viendo

50 Le señalas el ramen 

51 Te hace que no

52 Por favor

53 "Mío"

54 A chinga habló

55 Que loco

56 Le pides por favor y al final acepta

57 Cabron está chida

58 Muy chida de hecho

59 Te presentas, es como hablar con tarzán

60 Pero al final se hacen amigos

61 Cuando acaba el receso los ven juntos

62 Yyyyy el Isma y la china son novioooos

63 Son novios son novios

64 Te emputas y te vas a tu asiento

65 Todos se te quedan viendo

66 Y es que tampoco ayuda que cuando acabó la clase la pinche Toru caminó hasta tu lugar y se te quedó viendo

67 La mandas a la verga y te vas entre las risas de todos tus compañeros

68 Ella nomás se quedó ahí parada

69 Todos se van y ella se queda ahí

70 Al día siguiente ves a Toru llegar y ya ni te voltea a ver

71 Chale, chance si te pasaste de verga

72 Te awitas porque como que te quiere voltear a ver y se awita más

73 En el receso agarra y se va

74 Todos te ven feo y te quieres meter en la tierra

75 A la salida se sale también, se va caminando por la calle larga

76 Tu te apresuras a salir y te lanzas a comprarte tu manjar semanal

77 Tu pinche Maruchan de camarón 

78 Le comes

79 No sabe cómo la de Toru

80 Te awitas

81 En eso ves que de reojo va caminando en la otra banqueta

82 Se te ocurre un plan

83 Agarras tu Maruchan y te vas con ella

84 "Toru!"

85 No voltea

86 "Toru, perdón"

87 Ve que la estás siguiendo y camina más rápido

88 Te awitas viendo como se va y te le quedas viendo a tu Maruchan

89 En eso ves que se acerca

90 Le ofreces de tu Maruchan

91 Se le queda viendo

92 Chance si está pendeja

93 Agarra el tenedor y le come

94 "Mierda". Dice mientras señala tu maruchan

95 Bueno, al lado de sus fideos la maruchan si está culerita eh

96 Toru se ríe, en eso empieza a llover

97 Toru se asusta y busca algo en su mochila

98 No trae paraguas

99 Tu si traes, gracias jefa por meterme hasta los ojos furiosos a la mochila

100 Abres el paraguas y te cubres junto con ella

101 Se queda viendo pa arriba, a tu paraguas

102 Wey ya, admítelo, si está pendeja

103 "Casa?" Le dices

104 Cacha el pedo de que la quieres llevar pa que no se moje

105 Te dice que si y agacha la cabeza

106 Te aguantas las ganas de hacer sonido de besito como naco que eres

107 Caminan bajo tu paraguas, Toru te va guiando a su cantón

108 Total, en tu casa no hay nadie, ni van a saber si llegas tarde.

109 En el camino ves que Toru se puso toda roja, es que sus hombros se estaban tocando

110 Si, está pendeja

111 Total, llegan a su cantón y te da las gracias y se mete en chinga

112 Tu te vas a tu cantón pero te das cuenta de algo

113 Se clavó tu maruchan

114 No que no te gustó hijadelaberga?

115 Te regresas con hambre a tu casa y tienes que comerte unas pinches tunas que había en el refri

116 No mames, unas tunas

117 Al otro día Toru llega y se sienta al lado de ti

118 A que pedo

119 Te saluda bien quitada de la pena y todos empiezan a chingar

120 Hasta te apodan el COVID porque le diste a la chinita

121 Les quieres decir algo pero Toru ya te está escribiendo en la libreta

122 "No hagas caso"

123 Ya no quieres cagarla y terminas ignorando a esos weyes

124 Tomas la clase de grilla, que diga de historia, y empieza el receso 

125 Toru te dice que la sigas

126 De su tupper saca unos fideos

127 Huelen bien chido

128 En eso saca otro para ti

129 Alaberga

130 Comen juntos, esos fideos le están haciendo el amor a tu boca

131 "Mejor que maruchan" te dice Toru

132 Asientes energicamente

133 Terminan de comer y le das las gracias, cuando le pasas su tupper sus dedos se tocan

134 Toru se pone toda roja y tú te sacas de pedo

135 Está pendeja, pero pues hace fideos chidos

136 Desde ahí Toru te enseña a comer Ramen.

137 Así le dice a los fideos esos

138 Te pasa recetas para mejorar la maruchan y también te enseña animes que le gustan

139 Por ella viste Chobits

140 Joder Chobits, obra de arte audiovisual moderna

141 Poco a poco se comienzan a tontear el uno al otro y un día se te declara con una carta

142 "Quieres ser novio?"

143 Está pendeja, pero aceptas

144 Te toma la mano y se le queda viendo

145 Bueno ya, no se trata de estar diciendo que está pendeja cada cinco números

146 Tu aprietas su mano contra la de ella

147 Se ponen todos nerviosos y se saltan computación para estarse haciendo piojito

148 Y eso que fue hora libre y los dejaron jugar al sanandres en el proyector

149 Carajo

150 Tu y Toru en ese momento estaban más ocupados

151 Dándose su primer beso...

152 Desde ese día Toru se puso bien rara

153 Osea, más rara de lo normal

154 Derrepente te quería besar el cuello de la nada

155 Te ponía las manos en sus muslos cuando estaban en clase

156 Y hasta te dejaba sus calzones usados en tu mochila

157 Un día de plano se te acerca, se ve que estuvo practicando para decirlo de la manera más sexy posible a pesar de que no hablaba español

158 "Tengo casa sola"

159 En eso que se te para el chiliwili

160 "Después clases"

161 Le dices que si como pendejo

162 Ni sabes que viste en matematicas porque toda la sangre se te fue del cerebro a la pichula

163 Apenas sonó la campana de salida y Toru ya te había agarrado del brazo

164 Prácticamente te arrastró hacia su casa

165 Cuando entraron querías quitarle el cosplay de Peni Parker que siempre trae como pinche uniforme pero te detiene

166 "Preparé algo, comer primero"

167 Ves que sirve un plato de Ramen como rojo

168 "Tonkotsu ramen, especial, muy rico"

169 Te sienta a comer 

170 Es probablemente el mejor ramen que has comido en toda tu vida

171 Mientras comes Toru parece que se está excitando al verte comer

172 Empieza a respirar muy pesado y se muerde los labios

172 Le preguntas si no va a comer

173 "Comer después yo" te dice en medio de un suspiro

173 Le dices que está muy rico, que si te puede servir más

174 Lo hace, pero está vez es blanco y no sabe tan bueno

175 "Oye pero le falta algo"

176 "Puse ingrediente para ti antes"

177 Le preguntas que que es

178 En eso bien emocionada te dice que es algo que viene de lo más profundo de ella

179 Y saca una pinche kotex usada

180 VETE A LA VERGA

181 Te guacareas encima de la mesa, Toru se está riendo

182 Cuando vomitas ves que cae un pedacito de como de carne rosita que no es de animal

183 Te desmayas

184 Lo último que ves es como Toru te empieza a arrancar el pantalón

185 Cuando despiertas te sientes muy mareado

186 Ves como 5 condones usados en el piso y un paquetito de Saladitas

187 Las Saladitas son horneadas

188 Te lo chingas por pura hambre, no ves a Toru en ningún lado

189 Te pelas de ahí y llegando a tu casa te lavas la lengua con cloro

190 No mames el cloro es venenoso pendejo

191 Mueres, tentativamente a propósito

192 Cuando te están enterrando, de entre tus familiares, sale Toru y avienta a tu fosa una prueba de embarazo y se va

193 La prueba era positiva

—Umeboshi, con uno de sus ramen que vende por solo 45 pesos en UAM Iztapalapa (Ya no tiene de esos)'''


# Puedes usar la variable 'historia_mansion' en tu código como desees.

text_to_speech_and_save(texto, rate=150)
print("audio convertido")