import gradio as gr

def add_one(x):
    return x + 1

iface = gr.Interface(
    fn=add_one,
    inputs=gr.Number(label="Enter a number"),
    outputs="number",
    title="Add 1 to Your Input",
    description="Simple test app that adds 1 to your number"
)

iface.launch()
