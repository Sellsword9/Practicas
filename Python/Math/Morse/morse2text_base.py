"""
Execute a basic translation algorithm and register how much it takes 
"""
import time

translate= {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0'
}

def iterate_translation(text: str) -> str:
    c = ""
    for word in text.split():
        c += translate[word]
        c += " "
    return c.strip()

def measure_execution_time(algorithm, num_times: float, text: str) -> float:
    time_count: float = 0
    translation = "## Error: Translation was not accomplished ##"
    while (num_times > 0):
        start_time = time.time()  # Start the timer
        translation = algorithm(text)  # Execute the algorithm
        end_time = time.time()  # Stop the timer
        execution_time = end_time - start_time
        time_count += execution_time
        num_times = num_times - 1
    try:
        print(f"Translation is {translation} and it took {time_count} to translate it {num_times} times. Avg: {time_count / num_times}")
    except:
        print("float division by 0")

measure_execution_time(iterate_translation, 10e4, ". . ...--")