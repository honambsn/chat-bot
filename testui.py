import gradio as gr
import threading
import time

# Function to simulate Program 1
def program_1():
    while True:
        print("Program 1 is running...")
        time.sleep(1)

# Function to simulate Program 2
def program_2():
    while True:
        print("Program 2 is running...")
        time.sleep(1)

# Function to run the selected program
def run_program(selected_program):
    if selected_program == "Program 1":
        threading.Thread(target=program_1).start()
    elif selected_program == "Program 2":
        threading.Thread(target=program_2).start()

# Function to stop the current program
def stop_program():
    print("Stopping the current program...")

# Gradio interface
iface = gr.Interface(
    fn=None,
    inputs=[gr.Button("Program 1", run_program, "Program 1"),
            gr.Button("Program 2", run_program, "Program 2")],
    outputs=gr.Button("Stop", stop_program),
    title="Program Selector",
    description="Select a program to run or stop the current program."
)

iface.launch()
