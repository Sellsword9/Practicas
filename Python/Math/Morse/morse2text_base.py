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

def iterate_translation(text: str) -> float:
    c = ""
    for word in text.split(" "):
        c += translate[word]
        c += " "
    return c.strip

def measure_execution_time(algorithm: function, num_times: int, text: str) -> float:
    time: float = 0
    translation = "## Error: Translation was not accomplished ##"
    for _ in range(num_times):
        start_time = time.time()  # Start the timer
        translation = algorithm(text)  # Execute the algorithm
        end_time = time.time()  # Stop the timer
        execution_time = end_time - start_time
        total_time += execution_time
    
    print(f"Translation is {translation} and it took {time}")
