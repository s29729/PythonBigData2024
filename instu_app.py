import streamlit as st
import os
import subprocess

# Defining the directory where uploaded files will be stored
UPLOAD_DIRECTORY = "./uploaded_videos"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

#Defining directory for the generated file
OUTPUT_DIR = "./generated_files"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Video loader
def main():
    st.title("Create your instruction from the video")

    # File uploader
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:
        # Saving the uploaded video file to the defined directory
        file_path = os.path.join(UPLOAD_DIRECTORY, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully.")

        # Button to execute core_code Python code
        if st.button("Generate Instruction"):
            process_command = f"python core_code.py --input {file_path}"
            process_result = subprocess.run(process_command, shell=True, capture_output=True, text=True)

            # Results information
            if process_result.returncode == 0:
                st.success("Instruction created successfully.")
                
                output_file_path = os.path.join(OUTPUT_DIR, "instructions.docx")
                
                # Enable user to download the processed file
                with open(output_file_path, "rb") as file:
                    st.download_button(label="Download Instruction",
                                       data=file,
                                       file_name="instructions.docx",
                                       mime="docx")
                st.balloons()
            else:
                st.error("Failed to create instruction.")
                st.code(process_result.stderr)

if __name__ == "__main__":
    main()
