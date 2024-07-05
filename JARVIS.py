import speech_recognition as sr
import webbrowser
import os
import sys
import pyttsx3
import pywhatkit
import datetime
import pyautogui

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define responses for basic conversation, greetings, and responses

    # Define responses for basic conversation, greetings, and responses
conversations = {
    "whats your name?":"my name is JARVIS!",
    "how are you": "I'm just a computer program, so I don't have feelings, but thanks for asking!",
    "what can you do": "I can perform various tasks like searching the web, opening apps, adding notes, and playing music.",
    "tell me a joke": "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
    "who created you": "I was created by soham!",
    "stop": "Stopping the program.",
    "hi": "Hello! How can I assist you today?",
    "hello": "Hello! How can I assist you today?",
    "your_custom_command": "Your custom response goes here.",
    "another_command": "Another custom response.",
    "new_command": "A new custom response.",
    "yet_another_command": "Yet another custom response.",
    "ok": "is there anything else you wanna know?",
    "namaskar": "namaskar!",
    "how's the weather today": "I don't have real-time weather information. You can check a weather website or app for that.",
    "what's your favorite color": "I don't have preferences, but I think all colors are interesting!",
    "tell me a fun fact": "Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "can you recommend a book": "Certainly! One classic book I recommend is 'To Kill a Mockingbird' by Harper Lee.",
    "what's the capital of France": "The capital of France is Paris.",
    "how do you say 'hello' in Spanish": "In Spanish, 'hello' is 'hola.'",
    "what's the time": "I'm sorry, but I don't have real-time clock information. You can check the time on your device or ask a voice assistant like Siri or Google Assistant.",
    "tell me about yourself": "I'm just a computer program created to assist with various tasks and provide information.",
    "what's your favorite movie": "I don't have personal preferences, but some popular movies include 'The Shawshank Redemption' and 'The Godfather.'",
    "can you do math": "Yes, I can perform basic math calculations. Just ask me a math question!",
    "who won the last World Series": "I'm not sure about the most recent World Series winner. You can check a sports news website for the latest information.",
    "what's the meaning of life": "The meaning of life is a philosophical question that has been debated for centuries. It varies from person to person and can involve personal beliefs and values.",
    "do you have any siblings": "I don't have siblings. I'm a standalone computer program.",
    "where were you born": "I was created by developers at OpenAI, so you could say I was 'born' in the digital realm.",
    "what's your favorite food": "I don't eat, so I don't have a favorite food. However, I can help you find recipes or restaurants if you're looking for something specific!",
    "what's the best programming language": "The best programming language depends on the task you want to accomplish. Python, JavaScript, and Java are popular choices for various purposes.",
    "how's your day": "I don't experience days, but I'm here to assist you with your questions and tasks.",
    "tell me a riddle": "Sure, here's one: I'm not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
    "what's the largest planet in our solar system": "The largest planet in our solar system is Jupiter.",
    "can you play music for me": "Of course! Just tell me the name of the song you'd like to hear, and I'll try to play it for you.",
    "what's the square root of 144": "The square root of 144 is 12.",
    "do you believe in aliens": "I don't have personal beliefs, but the existence of extraterrestrial life is a topic of scientific interest and exploration.",
    "tell me a science fact": "Sure, here's one: Honey never spoils because its low water content and high acidity create an environment where bacteria and microorganisms can't survive.",
    "what's your favorite book": "I don't have preferences, but I can recommend popular books in various genres if you'd like.",
    "can you help me with my homework": "I can certainly try to help! Please provide the details of your homework question, and I'll do my best to assist you.",
    "what's the tallest mountain in the world": "The tallest mountain in the world is Mount Everest, which is part of the Himalayas.",
    "tell me a historical fact": "Sure, here's one: The Great Wall of China is the longest wall in the world and stretches over 13,000 miles.",
    "how do you pronounce 'schedule'": "The pronunciation of 'schedule' can vary between 'shed-yool' (UK) and 'sked-yool' (US).",
    "what's the meaning of 'carpe diem'": "'Carpe diem' is a Latin phrase that means 'seize the day' or 'make the most of the present moment.'",
    "can you recommend a movie": "Certainly! What genre are you in the mood for? I can recommend a movie based on your preferences.",
    "who's your favorite musician": "I don't have preferences, but there are many talented musicians in various genres. Is there a specific genre you're interested in?",
    "tell me a travel tip": "When traveling, it's a good idea to keep digital copies of important documents like your passport and travel itinerary in case they get lost or stolen.",
    "what's the largest ocean in the world": "The largest ocean in the world is the Pacific Ocean.",
    "tell me a joke about computers": "Sure, here's one: Why did the computer keep freezing? Because it left its Windows open!",
    "what's your favorite animal": "I don't have favorites, but there are many fascinating animals in the world. Is there a specific animal you'd like to learn more about?",
    "tell me a fun science experiment": "You can try the classic 'mentos and soda' experiment by dropping mentos candies into a bottle of soda to create a fizzy eruption.",
    "what's the speed of light": "The speed of light in a vacuum is approximately 299,792,458 meters per second (or about 186,282 miles per second).",
    "can you help me find a job": "I can provide tips and resources for job searching and creating a resume. What type of job are you looking for?",
    "what's the most popular sport in the world": "Soccer (or football) is often considered the most popular sport in the world, with a massive global following.",
    "tell me a quote from a famous person": "Certainly! Here's a quote from Albert Einstein: 'Imagination is more important than knowledge.'",
    "what's the meaning of 'serendipity'": "'Serendipity' refers to the occurrence of fortunate and unexpected events by chance or luck.",
    "can you recommend a good restaurant": "I can help you find restaurants in your area or provide recommendations based on your cuisine preferences.",
    "tell me a cooking tip": "When baking, you can use applesauce or mashed bananas as a healthier substitute for butter or oil in recipes.",
    "what's the longest river in the world": "The longest river in the world is the Nile River in Africa.",
    "tell me a famous painting": "One famous painting is the 'Mona Lisa' by Leonardo da Vinci, known for its enigmatic smile.",
    "what's the smallest country in the world": "The smallest country in the world is Vatican City, an independent city-state enclaved within Rome, Italy.",
    "tell me a space fact": "Sure, here's one: A day on Venus (the planet) is longer than its year. It takes Venus about 243 Earth days to rotate once on its axis but only about 225 Earth days to orbit the Sun.",
    "what's the highest-grossing movie of all time": "As of my last knowledge update, the highest-grossing movie of all time is 'Avatar,' directed by James Cameron.",
    "tell me a gardening tip": "To deter pests in your garden, consider planting companion plants that naturally repel insects, like marigolds and basil.",
    "what's the currency of Japan": "The currency of Japan is the Japanese Yen (¥).",
    "tell me a technology fact": "Sure, here's one: The first computer mouse was invented by Douglas Engelbart in 1964, and it was made of wood.",
    "what's the longest-running TV show": "The longest-running TV show is 'The Simpsons,' an animated series that has been on the air since 1989.",
    "tell me a space fact": "Sure, here's one: The largest volcano in the solar system is Olympus Mons on Mars, which is about 13.6 miles (22 kilometers) high.",
    "what's the largest desert in the world": "The largest desert in the world is the Antarctic Desert, covering the entire continent of Antarctica.",
    "tell me a technology fact": "Sure, here's one: The first email was sent by Ray Tomlinson in 1971. It was a test message sent between two machines that were side by side.",
    "what's the national flower of Japan": "The national flower of Japan is the cherry blossom, also known as the sakura.",
    "tell me a science experiment": "You can try the 'egg in a bottle' experiment by placing a peeled hard-boiled egg on the mouth of a bottle. When you heat the bottle, the egg gets sucked inside due to the change in air pressure.",
    "what's the population of China": "As of my last knowledge update, China is the most populous country in the world with over 1.4 billion people.",
    "tell me a fun fact about animals": "Sure, here's one: Octopuses have three hearts. Two pump blood to the gills, and one pumps it to the rest of the body.",
    "what's the smallest planet in our solar system": "The smallest planet in our solar system is Mercury.",
    "tell me a famous quote from a movie": "Here's a classic one: 'May the Force be with you,' from the 'Star Wars' franchise.",
    "what's the most spoken language in the world": "The most spoken language in the world is Mandarin Chinese, with over a billion native speakers.",
    "tell me a history fact": "Certainly! The Great Wall of China, built over several centuries, is over 13,000 miles long and is one of the most iconic historical landmarks.",
    "what's the capital of Australia": "The capital of Australia is Canberra.",
    "tell me a fun fact about space": "Sure, here's one: Space is completely silent because there is no air or medium to carry sound waves.",
    "what's the tallest tree in the world": "The tallest tree in the world is Hyperion, a coast redwood (Sequoia sempervirens) located in California, USA.",
    "tell me a famous quote from a scientist": "Here's one from Albert Einstein: 'Imagination is more important than knowledge.'",
    "what's the fastest land animal": "The fastest land animal is the cheetah, capable of reaching speeds up to 70 miles per hour (112 kilometers per hour).",
    "tell me a fun fact about music": "Certainly! The shortest song ever recorded is 'You Suffer' by the band Napalm Death. It's just 1.316 seconds long!",
    "what's the highest mountain in North America": "The highest mountain in North America is Denali, also known as Mount McKinley, located in Alaska, USA.",
    "tell me a fun fact about the human body": "Sure, here's one: Your taste buds have a lifespan of about 10 to 14 days, and new ones are constantly replacing old ones.",
    "what's the longest river in Asia": "The longest river in Asia is the Yangtze River, also known as the Chang Jiang.",
    "tell me a famous quote from a philosopher": "Here's one from Socrates: 'An unexamined life is not worth living.'",
    "what's the largest mammal in the world": "The largest mammal in the world is the blue whale, which can grow to lengths of over 100 feet (30 meters).",
    "tell me a fun fact about the ocean": "Certainly! The Pacific Ocean is the largest and deepest ocean on Earth, covering more than 60 million square miles (155 million square kilometers).",
    "what's the highest mountain in South America": "The highest mountain in South America is Mount Aconcagua, located in the Andes mountain range in Argentina.",
    "tell me a famous quote from a writer": "Here's one from Mark Twain: 'The two most important days in your life are the day you are born and the day you find out why.'",
    "what's the largest moon in our solar system": "The largest moon in our solar system is Ganymede, one of Jupiter's moons.",
    "tell me a fun fact about the human brain": "Certainly! The human brain has about 86 billion neurons, and it generates about 20 watts of electrical power when awake.",
    "what's the deepest part of the ocean": "The deepest part of the ocean is the Mariana Trench, specifically the Challenger Deep, which reaches a depth of about 36,070 feet (10,994 meters).",
    "tell me a famous quote from a leader": "Here's one from Mahatma Gandhi: 'You must be the change you wish to see in the world.'",
    "what's the smallest bird in the world": "The smallest bird in the world is the bee hummingbird, native to Cuba and Isla de la Juventud.",
    "tell me a fun fact about the Eiffel Tower": "Certainly! The Eiffel Tower in Paris, France, is made of iron and weighs approximately 10,100 tons.",
    "what's the largest desert in Africa": "The largest desert in Africa is the Sahara Desert, covering much of North Africa.",
    "tell me a famous quote from an artist": "Here's one from Pablo Picasso: 'Every child is an artist. The problem is how to remain an artist once we grow up.'",
    "what's the fastest bird in the world": "The fastest bird in the world is the peregrine falcon, which can reach speeds of up to 240 miles per hour (386 kilometers per hour) during its hunting stoop.",
    "tell me a fun fact about the Great Wall of China": "Certainly! The Great Wall of China is not a single continuous wall but a series of walls and fortifications built over different dynasties.",
    "what's the largest planet in our solar system": "The largest planet in our solar system is Jupiter.",
    "tell me a famous quote from a musician": "Here's one from Ludwig van Beethoven: 'Music can change the world.'",
    "what's the most widely spoken language in Africa": "The most widely spoken language in Africa is Arabic, due to its use in many North African countries.",
    "tell me a fun fact about elephants": "Sure, here's one: Elephants are known for their excellent memory. They can remember locations of water sources and even recognize other elephants they haven't seen in years.",
    "what's the tallest building in the world": "As of my last knowledge update, the tallest building in the world is the Burj Khalifa in Dubai, United Arab Emirates.",
    "tell me a famous quote from a movie character": "Here's one from Forrest Gump: 'Life is like a box of chocolates; you never know what you're gonna get.'",
    "what's the largest moon of Saturn": "The largest moon of Saturn is Titan, known for its thick atmosphere and lakes of liquid methane and ethane on its surface.",
    "tell me a fun fact about dolphins": "Certainly! Dolphins are known for their intelligence and social behavior. They often use a series of clicks and whistles to communicate with each other.",
    "what's the smallest planet in our solar system": "The smallest planet in our solar system is Mercury.",
    "tell me a famous quote from a historical figure": "Here's one from Martin Luther King Jr.: 'Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that.'",
    "what's the longest river in Europe": "The longest river in Europe is the Volga River, flowing through Russia.",
    "tell me a fun fact about penguins": "Sure, here's one: Penguins are native to the Southern Hemisphere and are found in a variety of climates, from the icy Antarctic to the temperate Galápagos Islands.",
    "what's the largest lake in Africa": "The largest lake in Africa by surface area is Lake Victoria, shared by Kenya, Tanzania, and Uganda.",
    "tell me a famous quote from a scientist": "Here's one from Isaac Newton: 'If I have seen further, it is by standing on the shoulders of giants.'",
    "what's the fastest fish in the ocean": "The fastest fish in the ocean is the sailfish, capable of swimming at speeds of up to 68 miles per hour (110 kilometers per hour).",
    "tell me a fun fact about the Great Barrier Reef": "Certainly! The Great Barrier Reef is the world's largest coral reef system and is visible from space. It's home to a diverse range of marine life.",
    "what's the highest waterfall in the world": "The highest waterfall in the world is Angel Falls in Venezuela, with a total height of 3,212 feet (979 meters).",
    "tell me a famous quote from a poet": "Here's one from Robert Frost: 'Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference.'",
    "what's the fastest land mammal": "The fastest land mammal is the cheetah, known for its incredible speed during hunts.",
    "tell me a fun fact about the Amazon Rainforest": "Certainly! The Amazon Rainforest is home to approximately 10 percent of the world's known species and produces 20 percent of the world's oxygen.",
    "what's the national bird of the United States": "The national bird of the United States is the bald eagle.",
    "tell me a famous quote from a philosopher": "Here's one from Aristotle: 'Happiness depends upon ourselves.'",
    "what's the largest bird in the world": "The largest bird in the world is the ostrich, known for its large size and running speed.",
    "tell me a fun fact about bees": "Sure, here's one: Bees communicate with each other through complex dance patterns known as the 'waggle dance' to indicate the location of food sources.",
    "what's the deepest lake in the world": "The deepest lake in the world is Lake Baikal in Siberia, Russia, known for its unique biodiversity.",
    "tell me a famous quote from a leader": "Here's one from Winston Churchill: 'Success is not final, failure is not fatal: It is the courage to continue that counts.'",

}

# Add more commands and responses as needed

last_command_time = datetime.datetime.now()

# Function to perform actions based on recognized commands
def perform_action(command):
    global last_command_time  # Access the global variable

    try:
        # Update the last command time
        last_command_time = datetime.datetime.now()
    except Exception as e:
        speak(f"An error occurred: {e}")

# Function to perform actions based on recognized commands
def perform_action(command):
    try:
        if "search" in command:
            search_query = command.split("search", 1)[1].strip()
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            speak("Searching for " + search_query)
        elif "add note" in command:
            note = command.split("add note", 1)[1].strip()
            with open("notes.txt", "a") as file:
                file.write(note + "\n")
            speak("Note added: " + note)
        elif "date" in command:
            tell_day_and_date()
        elif "what's the time" in command or "what is the time" in command:
            time_response = get_current_time()
            speak(time_response)
        elif "calculate math" in command:
            # Extract the mathematical expression from the command
            expression = command.split("calculate math", 1)[1].strip()
            calculate_math_expression(expression)  
        elif "take a screenshot" in command:
            take_screenshot()
        elif "delete previous screenshot" in command:
            delete_latest_screenshot()          
        elif "open" in command:
            app_name = command.split("open", 1)[1].strip()
            open_app(app_name)
        elif "close" in command:
            app_name = command.split("close", 1)[1].strip()
            close_app(app_name)
        elif "play" in command:
            song_query = command.split("play", 1)[1].strip()
            play_music(song_query)
        elif "stop" in command:
            speak("Stopping the program.")
            sys.exit()
        elif command.lower() in conversations:
            speak(conversations[command.lower()])
        else:
            speak("Command not recognized.")
    except Exception as e:
        speak(f"An error occurred: {e}")

# Function to open an application by name
def open_app(app_name):
    try:
        os.system(f'start {app_name}')  # On Windows
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"Could not open {app_name}: {e}")

# Function to close an application by name
def close_app(app_name):
    try:
        os.system(f'taskkill /im {app_name}.exe /f')  # On Windows, force close the app
        speak(f"Closing {app_name}.")
    except Exception as e:
        speak(f"Could not close {app_name}: {e}")

# Function to play music from YouTube
def play_music(song_query):
    try:
        pywhatkit.playonyt(song_query)
        speak(f"Playing the song {song_query} on YouTube.")
    except Exception as e:
        speak(f"An error occurred: {e}")

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to determine the time of day and provide a greeting
def get_time_greeting():
    current_time = datetime.datetime.now()
    if 5 <= current_time.hour < 12:
        return "Good morning! How can I assist you today?"
    elif 12 <= current_time.hour < 17:
        return "Good afternoon! How can I assist you today?"
    else:
        return "Good evening! How can I assist you today?"


# function that tells the present date  
def tell_day_and_date():
    try:
        # Get the current date and day
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")  # date in YYYY-MM-DD format
        day = now.strftime("%A")  # day of the week

        speak(f"Today is {day}, {date}")
    except Exception as e:
        speak(f"An error occurred while getting the day and date: {e}")

# function that tells the current time
def get_current_time():
    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%I:%M %p")  # Format time as "hh:mm AM/PM"
    return f"The current time is {time_str}"

# Function to solve a math problem or open solving website
def calculate_math_expression(expression):
    try:
        # Evaluate the mathematical expression
        result = eval(expression)
        speak(f"The result of {expression} is {result}")
    except Exception as e:
        speak(f"An error occurred while calculating the expression: {e}")
        open_math_problem_website()

def open_math_problem_website():
    math_website_url = "https://www.wolframalpha.com/"  # Change to the desired math website URL
    webbrowser.open(math_website_url)
    speak("I couldn't recognize the math expression. Opening a math problem-solving website for you.")

# function to take a screenshot
def take_screenshot():
    try:
        # Capture the screen
        screenshot = pyautogui.screenshot()

        # Define the path to save the screenshot
        screenshot_path = "screenshots"

        # Create the 'screenshots' directory if it doesn't exist
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        # Generate a unique filename based on the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_filename = os.path.join(screenshot_path, f"screenshot_{timestamp}.png")

        # Save the screenshot
        screenshot.save(screenshot_filename)

        speak(f"Screenshot taken and saved as {screenshot_filename}")
    except Exception as e:
        speak(f"An error occurred while taking a screenshot: {e}")


# function to delete the latest screenshot

def delete_latest_screenshot():
    try:
        screenshot_path = "screenshots"

        # Get a list of all screenshot files in the directory
        screenshot_files = [f for f in os.listdir(screenshot_path) if f.endswith(".png")]

        # Check if there are any screenshot files
        if screenshot_files:
            # Find the latest screenshot based on file creation time
            latest_screenshot = max(screenshot_files, key=lambda x: os.path.getctime(os.path.join(screenshot_path, x)))

            # Delete the latest screenshot
            screenshot_file = os.path.join(screenshot_path, latest_screenshot)
            os.remove(screenshot_file)

            speak(f"Latest screenshot '{latest_screenshot}' has been deleted.")
        else:
            speak("No screenshots found to delete.")
    except Exception as e:
        speak(f"An error occurred while deleting the latest screenshot: {e}")



##############################################################################################
# Main loop to listen for voice commands when "Jarvis" is said
from playsound import playsound

while True:
    with sr.Microphone() as source:
        playsound("D:\project 1\listening_sound.mp3")
        print("Listening...")
        speak("now listening!")
        audio = recognizer.listen(source)


    try:
        # Recognize the speech using Google Web Speech API
        trigger_word = recognizer.recognize_google(audio).lower()
        print("You said:", trigger_word)

        if "jarvis" in trigger_word:
            greeting = get_time_greeting()
            speak(greeting)
            while True:
                playsound("D:\project 1\listening_sound.mp3")
                with sr.Microphone() as source:
                    print("Listening for commands...")
                    audio = recognizer.listen(source)
                
                try:
                    # Recognize the speech for commands
                    command = recognizer.recognize_google(audio).lower()
                    print("You said:", command)
                    perform_action(command)
                
                    # Check for the "stop" command to exit the inner loop
                    if "stop" in command:
                        speak("Stopping listening.")
                        break
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            # Check if the program has been idle, exit's if so
        current_time = datetime.datetime.now()
        if (current_time - last_command_time).total_seconds() >= 10:  #timeout
            speak("No activity detected. Exiting the program.")
            sys.exit()

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")










