import pyttsx3

def get_available_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    return voices

def text_to_speech_and_save(text: str, file_name: str = "audio.mp3", rate: int = 150, voice_id: int = 0) -> None:
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    voices = get_available_voices()

    # Selecciona la voz deseada
    if 0 <= voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
    else:
        print("Índice de voz no válido. Se usará la voz predeterminada.")

    engine.save_to_file(text, file_name)
    engine.runAndWait()

# Ejemplo de uso
texto = """Neta que si no la armaron en la escuela y les gusta el chisme, vénganse a trabajar a un Elektra

Llevo cuatro años chambeando en uno desde que dejé el CECyTEM y neta que es la reverenda cábula

Te pasa de todo

Gente que llora para que le perdones los diecisiete mil pesos que deben de su moto

Batos bien desconectados que se quieren chingar las teles de muestra

Hasta señoras de sesenta años o más que nomas van para decirte que te invitan a salir

Pero nada como la vez que vi como un cabrón se cambió el fundillo a TELCEL

Todo empezó un miércoles de weba

Me había servido mi segundo vaso de café legal del día porque no me acababa de despertar

Me acomodé en mi estación de trabajo y nomás de pura mamada me asomé al frente

Al fondo solo estaban mis compañeros de trabajo y el wey de los celulares

Ese wey no trabajaba ahí, pero era el que activaba las sim de los teléfonos nuevos y le movía para meterles plan a la gente y todo

Era medio ondeado porque siempre llegaba temprano y no le hablaba a nadie, nomás se sentaba en su stand de plástico que estaba en la entrada y se la pasaba jugando clash con el internet de la tienda y contestando whatsapps

Normalmente me valdría verga verlo ahí sentado pero algo dentro de mi me dijo “quédatele viendo quédatele viendo”

Y en efecto, no pasaron ni treinta segundos y un cabron se mete corriendo a la tienda y le clava un sapezote en la choya que hasta brincó 

No mames sonó como si estuviera haciendo sopes

El pobre pendejo sale volando y cae hecho mierda en el piso con todas sus sim regadas al mismo tiempo que escucho que ese cabron le dice la mamada del siglo

“Te dije que no se la podías meter por el culo a la Fátima culero!" 

Y que le empieza a pegar en el piso

Yo ya sabía que el wey de los teléfonos estaba bien ondeado pero de la nada el hijo de su putamadre saca su spiderman interior y se para de un salto y comienzan a cruzar vergazos como si fuera dragon bol seta

Yo para ese momento ya había agarrado mis mantecadas y estaba viendo desde un asiento privilegiado el desmadre

Pensé que no se podía poner mejor cuando en eso llega una morra de pantalón pegado y cara de que vivía en Cuautepec

Presumiblemente era la Fátima

Que le grita al wey que llegó “¡Ya Juan Carlos, te dije que no me dolió!”

Ni la pelaron los dos pendejos y se siguieron dando madrazos

Pero te juro que hasta neta escupí el café cuando el cabrón de los celulares como que agarró vuelo y midió la distancia para meterle una patada voladora como en naruto al otro cabron pero le calculó mal y le cayó encima a la Fátima

Se pasó de verga pero wey, la pendeja chilló como si fuera pollo de hule asi de iiiiiiiiiiiuuuuuuuuuu

Me tapé la boca de un vergazo y hasta me voltearon a ver de lo fuerte que me reí

En medio de la confusión aprovechó el wey de los celulares para salirse corriendo alv de ahí y hasta lo perdí de vista

Me le quedé viendo a los dos pendejos que se lo fueron a verguear y no fue sino porque ellos voltearon a ver me di cuenta de que otra morra lo volvió a meter a la tienda de un cabezazo

Por como le hablaba, era su novia, o bueno, ex novia

La morra era más alta que ese wey y estaba toda vestida de negro como si fuera el undetaker

Nomás escuché que el wey de los celulares gritó “No mi amor, no es lo que crees deja te expli-”

Cual deja te explico, que lo carga y lo avienta contra el piso y lo empieza a pisar

En eso que los otros dos cabrones se unen a la morra undertaker y que también le empiezan a soltar pvtazos

Le estaban dando su verguiza al chaz chaz

Ni me dí cuenta que mis compañeros estaban todos paniqueados metidos en la sala de empleados llamando a los de seguridad porque todavía no habían llegado y que me dicen “No mames Paco no te vayan a pegar a ti ya metete”

Me valió verga

Wey hasta me dieron ganas de grabar

Y me arrepiento de no haberlo hecho

Porque todo esto no fue lo peor de todo 

Despues de dejarlo hecho mierda, el cabrón del zape que le baja los pantalones al de los celulares y le dice “Ahora vas a sentir como nos cobramos estas pendejadas en Jalisco”

Y vete a la chipileta que lo empieza a nalguear y a meterle los dedos en la cola

Ya se iba a bajar los pantalones para meterle el chiliwili cuando vió que la tira ya lo iba a trampar y que se le ocurre la estupidez que dejó pendejo hasta a Einstein

Que agarra una tarjeta sim, se agacha y se la pasa como cuatro veces en toda la raya del pedorro al otro culero 

Pagó a crédito con abonos chiquitos el hijo de suptm

Por fin llegaron los weyes de vigilancia y que se llevan a todos al MP 

Yo fingí demencia y pues no me llevaron a pesar de que vi todo

Lo que si es que el wey de los celulares cuando lo pararon estaba grite y grite que sentía algo en el recto y no paraba de sangrar

Se lo llevaron a la patrulla y de ahí no supe más de él

Pero cuando me acerqué a donde se estaban peleando me fijé y la pinche tarjeta sim se le había despegado el chip y probablemente eso es lo que tenía ensartado en el cacorro el pendejete ese XDDDDDDDDDDDDDDDDDDDDD

Desde ese día ya no ofrecemos planes con nuestros celulares en la tienda y mejor tenemos ya las tarjetas sim prepagadas y dejamos que los clientes se hagan bolas con los planes

Pero quién sabe si en una de esas él anillo de ese compa si tenga 500 megas para navegar y llamadas ilimitadas por 299 pesos al mes

—Umeboshi"""
# Obtén la lista de voces disponibles
voices = get_available_voices()
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name}")

# Elige la voz que prefieras
selected_voice = 0  # Cambia esto al índice de la voz que prefieras

text_to_speech_and_save(texto, file_name="audio.wav", rate=170, voice_id=selected_voice)
print("Audio convertido")
