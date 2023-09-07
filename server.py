from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('interface.html')


@app.route('/correct', methods=['POST'])
def correct():
    try:
        sentence = request.json['sentence']
        print("Input sentence:", sentence)
        
        # Execute the script and capture the output
        correction_output = subprocess.check_output(['python', 'python/correction.py', sentence], stderr=subprocess.STDOUT).decode('utf-8').strip()
        
        # Print the output to the server terminal
        print("Output from correction.py:", correction_output)
        
        # Split the output by newline and get the last line
        lines = correction_output.split('\n')
        corrected_sentence = lines[-1].strip()
        print("Corrected sentence:", corrected_sentence)
        
        return jsonify(correctedSentence=corrected_sentence)
    
    except subprocess.CalledProcessError as e:
        # Handle subprocess errors by printing the error and returning an error response
        error_message = str(e.output, 'utf-8')
        print("Error from subprocess:", error_message)
        return jsonify(error=error_message)

    except Exception as e:
        # Handle other exceptions (e.g., JSON parsing error) and log them
        error_message = str(e)
        print("Unhandled exception:", error_message)
        return jsonify(error=error_message)


if __name__ == '__main__':
    app.run(debug=True)
