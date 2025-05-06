import gradio as gr 

def combine_texts(t1, t2):
    return str(t1) + str(t2)

app = gr.Interface(
    fn = combine_texts,
    
    inputs = [
        gr.Textbox(),
        gr.Textbox()
    ],
    outputs = gr.Text()


)
app.launch(server_name="127.0.0.1", server_port= 7861)