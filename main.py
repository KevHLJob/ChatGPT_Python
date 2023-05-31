import openai
import config
import typer
from rich import print
from rich.table import Table

openai.api_key =config.api_Key
    
print("💭[bold blue]ChatGPT con Python by: KevDev[/bold blue]")
table= Table("COMANDO", "Descripción")
table.add_row("exit", "Salida del chat")
table.add_row("new", "Nueva conversación")
print(table)

def main():
#Contexto del asistente, example: eres un asistente útil
    context = {"role": "system",
                "content": "Eres un asistente muy útil"}
    #la variable guarda el contexto
    messages= [context]
    # mientras sea verdadero llama la función prompt para preguntar
    while True:
        content = __prompt()
    
        #si escribes new crea un nuevo contexto
        if content == "new":
            print("👍Nueva conversación creada")

            messages= [context]
            content = __prompt()


            
        messages.append({"role":"user","content":content})
        #en la variable se agrega el model y su contexto
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        
        #Esta variable muestra la respuesta de chatgpt con el contexto respectivo.
        response_content =response.choices[0].message.content
        
        messages.append({"role":"assistant","content":response_content})

        
        #respuesta trae el arreglo, con el mensaje y la respuesta de Chatgpt
        print(f"[blue]{response_content}[/blue]")
    
    

    #función de prompt que llama a la pregunta
def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar?")
    #si escribes exit, te aparece msj de confirmación
    if prompt == "exit":
      exit = typer.confirm("❗¿Desea salir del programa?") 
      #si es verdadero llama la función abort de typer
      if exit:
        print("👋Hasta luego")
        raise typer.Abort()
      #sino llama prompt nuevamente para preguntar...
      return __prompt()
    return prompt

#inicializa el main
if __name__ == "__main__":
    typer.run(main)