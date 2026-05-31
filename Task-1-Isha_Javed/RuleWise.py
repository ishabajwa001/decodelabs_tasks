responses = {

    # Greetings -- no explanation
    "hello" :{
        "response":("Hey there! {name} I'm RuleWise .\n Your guide to understanding Rule-Based AI!\n"
        "Type 'help' to get started"),
        "explain": False
    },
    "hi":{
        "response":("Hi! {name} Great to see you here .\n I'm RuleWise your friendly guide to help you understand Rule-Based Chatbots!\n"
        "Type 'help' to get started"),
        "explain": False
    },
    "hey":{
        "response":("Hey! {name} I'm here and ready to chat.\n Ask me anything about Rule-Based Chatbots!\n"
        "Type 'help' to get started"),
        "explain": False
    },
    "good morning":{
        "response":("Good morning!\n Ready to learn about rule-based AI today\n"
        "Type 'help' to get started"),
        "explain": False
    },
    "good night":{
        "response":("Good night!\n"),
        "explain": False
    },

    # Help -- no explanation
    "help": {
            "response": (
                "Ask me any of these and I will explain it to you:\n"
                "I recommend starting with 'what is a rule based chatbot'\n"
                "to get a solid foundation!\n\n"
                "  - What is a rule-based chatbot\n"
                "  - How do you work\n"
                "  - How do you match my input\n"
                "  - What is a knowledge base\n"
                "  - What is sanitization\n"
                "  - What is a fallback\n"
                "  - What is a loop\n"
                "  - Advantages of rule-based AI\n"
                "  - Disadvantages of rule-based AI\n"
                "  - Difference between you and ChatGPT\n"
                "If you want to see all the questions I can answer, just ask 'list all the questions'!"
            ),
            "explain": False
        },

    # List of Questions -- without explanation (since it's just a list of questions)
    "list all questions":{
            "response": (
                "Here are all the questions you can ask me:\n\n"
                "  - What is a rule-based chatbot\n"
                "  - What is a chatbot\n"
                "  - What is rule based\n"
                "  - Explain rule based chatbot\n"
                "  - What is AI\n"
                "  - What is machine learning\n"
                "  - What is the difference between AI and rule based chatbot\n"
                "  - How do you work\n"
                "  - How do you understand me\n"
                "  - How do you find answers\n"
                "  - What is a knowledge base\n"
                "  - What is dictionary\n"
                "  - What is sanitization\n"
                "  - What is normalization\n"
                "  - What is fallback\n"
                "  - What is loop\n"
                "  - What is while true\n"
                "  - What happens when you don't understand\n"
                "  - How do you match my input\n"
                "  - What is keyword matching\n"
                "  - What is intent\n"
                "  - Advantages of rule based chatbots\n"
                "  - Disadvantages of rule based chatbots\n"
                "  - Benefits of rule based chatbots\n"
                "  - Limitations of rule based chatbots\n"
                "  - Can you learn\n"
                "  - Can you learn new things\n"
                "  - Are you smart\n"
                "  - Do you think\n"
                "  - Do you understand me\n"
                "  - What is ChatGPT\n"
                "  - Difference between you and ChatGPT\n"
            ),
            "explain": True
    },

    # Concepts and Answers  -- witg explanations
    "what is a rule_based chatbot":{
            "response":(
                "A rule-based chatbot is a program that responds\n"
                "to user input using a fixed set of predefined rules.\n"
                "It matches what you type to a stored keyword\n"
                "and returns a stored answer.\n"
                "It does NOT learn, think, or understand language."
        ),
            "explanation":("This is the core concept! The keyword phrase matched a stored educational definition."),
            "explain": True
    },
        "what is a rulebased chatbot":{
            "response":(
                "A rule-based chatbot is a program that responds\n"
                "to user input using a fixed set of predefined rules.\n"
                "It matches what you type to a stored keyword\n"
                "and returns a stored answer.\n"
                "It does NOT learn, think, or understand language."
        ),
            "explanation":("This is the core concept! The keyword phrase matched a stored educational definition."),
            "explain": True
    },
    "what is a chatbot": {
            "response":(
                "A chatbot is a computer program that simulates conversation with humans.\n"
                "There are two main types:\n"
                "  1. Rule-Based Chatbots (like me!) - follow fixed rules\n"
                "  2. AI Chatbots (like ChatGPT) - learn from data"
            ),
            "explanation":("The keyword 'chatbot' matched a stored definition rule in my knowledge base."),
            "explain":True
    },
    "what is rule based":{
            "response":(
                "Rule-based means the system follows a strict set of IF-THEN rules.\n"
                "Example: IF user says 'hello' THEN reply 'Hi there!'\n"
                "Every response is decided by the programmer, not by the machine."
            ),
            "explanation":("The keyword 'rule based' matched a stored definition rule in my knowledge base."),
            "explain": True
    },
    "explain rule based chatbot":{
            "response":(
                "A rule-based chatbot works like this:\n"
                "  Step 1 - User types a message\n"
                "  Step 2 - Bot cleans the input (lowercase, remove spaces)\n"
                "  Step 3 - Bot searches its dictionary for a matching keyword\n"
                "  Step 4 - If found - returns stored reply\n"
                "  Step 5 - If not found - returns fallback response\n"
                "  Step 6 - Loop repeats for next input"
            ),
            "explanation": ("This matched an explanation rule that walks through the full chatbot process step by step"),
            "explain" : True
    },

    # Educational Concepts(AI , machine learning)-- with explanations 
    "what is ai":{
            "response":(
                "AI stands for Artificial Intelligence.\n"
                "It is the simulation of human intelligence by machines.\n"
                "AI includes learning, reasoning, and problem-solving.\n"
                "But I am NOT true AI - I just follow fixed rules!"
            ),
            "explanation":("The keyword 'what is ai' matched a stored definition in my knowledge base."),
            "explain" : True
    },
    "what is machine learning":{
            "response":(
                "Machine Learning is a branch of AI where computers learn from data.\n"
                "They improve over time without being explicitly programmed.\n"
                f"I do NOT use machine learning - my responses are 100% hardcoded."
            ),  
            "explanation":("The keyword 'machine learning' matched a stored educational definition. However, ml is not relevant to my rule-based design, so i also explained that I do not use it!"),
            "explain": True
    },

    # Comparison between Rule-Based and AI Chatbots -- with explanations
    "what is the difference between ai and rule based chatbot":{
            "response":(
                "Great question! Here's the difference:\n"
                "  Rule-Based Bot (Me):\n"
                "    - Follows fixed rules\n"
                "    - Cannot learn\n"
                "    - Fast and predictable\n"
                "    - Limited knowledge\n\n"
                "  AI Chatbot (ChatGPT):\n"
                "    - Learns from data\n"
                "    - Understands context\n"
                "    - Can handle new questions\n"
                "    - Much more flexible"
            ),
            "explanation":("This matched a comparison rule that highlights the key differences between rule-based and AI chatbots."),
            "explain": True
    },

    # ChatGPT Comparison -- with explanations
    "what is chatgpt":{
            "response":(
                "ChatGPT is an AI chatbot developed by OpenAI.\n"
                "It uses machine learning to understand and generate human-like text.\n"
                "Unlike me, ChatGPT can learn from data and improve over time.\n"
                "ChatGPT can handle complex conversations and understand context,\n"
                "while I can only respond to specific keywords based on fixed rules."
            ),
            "explanation":("This explains the key differences between ChatGPT, an AI chatbot, and me, a rule-based chatbot."),
            "explain": True
    },
    "difference between you and chatgpt":{
            "response":(
                "The difference between me and ChatGPT is:\n"
                "  Me (RuleWise):\n"
                "    - Rule-based chatbot\n"
                "    - Follows fixed rules\n"
                "    - Cannot learn or adapt\n"
                "    - Limited to pre-programmed knowledge\n\n"
                "  ChatGPT:\n"
                "    - AI chatbot\n"
                "    - Learns from data\n"
                "    - Can understand context\n"
                "    - Can handle new and complex conversations"
            ),
            "explanation":("This provides a direct comparison between my rule-based design and ChatGPT's AI capabilities."),
            "explain": True
    },

    # Process Explanation -- with explanations (explanation about how the chatbot works)
    "how do you work" :{
            "response":(
                "I work by following a simple process:\n"
                "  1. You type a message\n"
                "  2. I clean the input (lowercase, remove spaces)\n"
                "  3. I search my dictionary for a matching keyword\n"
                "  4. If I find a match - I return the stored reply\n"
                "  5. If no match - I return a fallback response\n"
                "  6. Loop back to step 1 for the next message"
            ),
            "explanation":("This matched an explanation rule that walks through the full chatbot process step by step."),
            "explain": True
    },
    "how do you understand me":{
            "response":(
                "Honestly I don't truly understand you!\n"
                "I just search for matching keywords in your text.\n"
                "If your message contains a keyword I know - I reply.\n"
                "If not - I give a fallback response.\n"
                "There is NO real understanding happening.\n",
                "This is a key insight - rule-based bots simulate understanding through matching, not real comprehension."
            ),
            "explanation":("This is a key insight - rule-based bots simulate understanding through matching, not real comprehension."),
            "explain": True
    },
    "how do you find answers":{
            "response":(
                "I find answers by looking up your cleaned input\n"
                "in a Python dictionary using the .get() method.\n"
                "Example: responses.get('hello', 'I don't understand')\n"
                "This returns the stored answer instantly in O(1) time!"
            ),
            "explanation":("This explains the mechanism behind how I retrieve responses from my knowledge base."),
            "explain": True
    },

    # Data Structure and Technical Concepts -- with explanations
    "what is a knowledge base":{
            "response":(
                "A knowledge base is the dictionary that stores all my rules.\n"
                "It contains KEY-VALUE pairs:\n"
                "  KEY = what the user types (e.g. 'hello')\n"
                "  VALUE = what I reply (e.g. 'Hi there!')\n"
                "My entire intelligence lives inside this dictionary."
            ),
            "explanation":"The keyword 'knowledge base' matched a stored explanation of how my data is structured.",
            "explain": True
    },
    "what is dictionary":{
            "response":(
            "In Python, a dictionary stores data as KEY:VALUE pairs.\n"
            "Example:\n"
            "  responses = {\n"
            "    'hello' : 'Hi there!',\n"
            "    'bye'   : 'Goodbye!'\n"
            "  }\n"
            "I use a dictionary to store all my rules.\n"
            "It gives instant lookup speed - O(1) complexity!"
            ),
            "explanation":("The keyword 'dictionary' matched a technical explanation of the data structure I use to store my rules."),
            "explain": True
    },
    "what is sanitization":{
            "response":(
                "Sanitization means cleaning the user input before processing.\n"
                "I do two things:\n"
                "  1. .lower()  - converts 'HELLO' to 'hello'\n"
                "  2. .strip()  - removes extra spaces '  hello  ' - 'hello'\n"
                "This ensures 'Hello', 'HELLO', and 'hello' all match the same rule."
            ),
            "explanation":("The keyword 'sanitization' matched a stored explanation of input cleaning - Phase 1 of my process"),
            "explain":True
    },
    "what is normalization":{
            "response":(
                "Normalization is the process of converting input into a standard format.\n"
                "For me, it means converting everything to lowercase.\n"
                "So 'HeLLo', 'HELLO', 'hello' all become 'hello'\n"
                "and can match the same dictionary key.",
            ),
            "explanation":("The keyword 'normalization' matched a stored explanation of the standardization process."),
            "explain":True
    },
    "what is fallback":{
            "response":(
                "A fallback is a default response when no rules match.\n"
                "If you type something I don't understand - I return a fallback reply.\n"
                "Example: 'I don't understand that. Can you rephrase'"
            ),
            "explanation":("The keyword 'fallback' matched a stored explanation of how I handle unmatched input - Phase 5 of my process."),
            "explain": True
    },
    "what is loop":{
            "response":(
                    "A loop keeps the chatbot running continuously.\n"
                "I use a 'while True' loop in Python:\n"
                "  while True:\n"
                "      user_input = input('You: ')\n"
                "      if user_input == 'exit': break\n"
                "      # process and reply...\n"
                "This loop is the HEARTBEAT of my system - it never stops until you exit."
            ),
            "explanation":("The keyword 'loop' matched a stored explanation of the while loop - the core execution mechanism"),
            "explain": True
    },
    "what is while true":{
            "response":(
                "while True' is a Python loop that runs forever.\n"
                "It keeps asking for input, processing it, and replying.\n"
                "The only way to stop it is a 'break' command.\n"
                "For chatbots, this creates a continuous conversation."
            ),
            "explanation":("The phrase 'while true' matched a technical explanation of the infinite loop structure."),
            "explain": True
    },

    # Fallback Mechanism and Matching Process -- with explanations
    "what happens when you don't understand":{
            "response":(
                "When I don't understand, I return my fallback response.\n"
                "This is stored as the default value in my .get() method.\n"
                "Example: responses.get('unknown', 'I don't understand')\n"
                "Since 'unknown' is not in my dictionary, the default is returned."
            ),
            "explanation":("This demonstrates the fallback mechanism - a critical part of any rule-based system."),
            "explain": True
    },
    "how do you match my input":{
            "response":(
                "I match your input using EXACT keyword matching.\n"
                "After cleaning your input, I look for it in my dictionary.\n"
                "If 'hello' is in my dictionary - match found!\n"
                "If 'what is love' is not - no match - fallback."
            ),
            "explanation":("This explains my exact matching behavior - a key characteristic of rule-based systems"),
            "explain": True
    },
    "what is keyword matching":{
            "response":(
                "Keyword matching means finding a specific word or phrase\n"
                "in the user's input and using it to select a response.\n"
                "Example: User types 'what is ai'\n"
                "Bot finds 'what is ai' in dictionary - returns stored answer.\n"
                "No understanding - just pattern matching!"
            ),
            "explanation":("The phrase 'keyword matching' triggered a stored explanation of the core matching technique used in rule-based chatbots."),
            "explain": True
    },
    "what is intent":{
            "response":(
                "An intent is the PURPOSE behind what a user types.\n"
                "Example: 'hello', 'hi', 'hey' all have the same intent - GREETING\n"
                "In rule-based bots, each keyword represents one intent.\n"
                "In AI bots, the system figures out intent automatically."
            ),
            "explanation":("The keyword 'intent' matched a stored explanation of intent classification in chatbots."),
            "explain": True
    },

    # Advantages and Disadvantages -- with explanations
    "advantages of rule based chatbots":{
            "response":(
                "Advantages of Rule-Based Chatbots:\n"
            "   Fast - instant responses\n"
            "   Predictable - always same answer for same input\n"
            "   Safe - zero hallucination risk\n"
            "   Transparent - you can read every rule\n"
            "   No training data needed\n"
            "   Works great for FAQs and simple tasks"
            ),
            "explanation":("This matched a stored list of advantages, highlighting the strengths of rule-based systems."),
            "explain": True
    },
    "disadvantages of rule based chatbots":{
            "response":(
                "Disadvantages of Rule-Based Chatbots:\n"
                "   No learning - can't improve over time\n"
                "   Limited knowledge - only what is programmed\n"
                "   Rigid - can't handle unexpected input\n"
                "   No understanding - just pattern matching\n"
                "   Can become unmanageable with many rules\n"
                "   Not suitable for complex conversations"
            ),
            "explanation":("This matched a stored list of disadvantages, highlighting the limitations of rule-based systems."),
            "explain": True
    },
    "what are the benefits of rule based chatbots":{
            "response":(
                "Benefits of Rule-Based Chatbots:\n"
                "   Fast and efficient for simple tasks\n"
                "   Easy to understand and debug\n"
                "   No risk of inappropriate responses\n"
                "   Great for handling FAQs\n"
                "   Can be built without data or AI expertise\n"
                "   Provides a clear structure for responses"
            ),
            "explanation":("This matched a stored list of benefits, emphasizing the practical advantages of rule-based chatbots."),
            "explain": True
    },
    "what are the limitations of rule based chatbots":{
            "response":(
                "Limitations of Rule-Based Chatbots:\n"
                "   Cannot learn or adapt\n"
                "   Limited to pre-programmed knowledge\n"
                "   Struggles with complex conversations\n"
                "   No true understanding of language\n"
                "   Can become unwieldy with many rules\n"
                "   Not ideal for dynamic or open-ended interactions"
            ),
            "explanation":("This matched a stored list of limitations, emphasizing the practical drawbacks of rule-based chatbots."),
            "explain": True
    },
    # Real-World Usage -- with explanations
    "do companies use rule based chatbots": {
        "response": (
            "Yes! Rule-Based Chatbots are widely used in industries worldwide:\n\n"
            "   Banking (e.g. HBL, MCB, Standard Chartered)\n"
            "     - Balance inquiries, account FAQs, branch info\n\n"
            "   Healthcare (e.g. hospital websites)\n"
            "     - Appointment booking, symptom checkers\n\n"
            "   E-Commerce (e.g. Daraz, Amazon)\n"
            "     - Order tracking, return policy, delivery FAQs\n\n"
            "   Telecom (e.g. Jazz, Zong, Telenor)\n"
            "     - Package info, bill inquiries, recharge help\n\n"
            "   Airlines (e.g. PIA, Emirates)\n"
            "     - Flight status, baggage policy, booking FAQs\n\n"
            "   AI Safety (e.g. NVIDIA NeMo, Meta Llama Guard)\n"
            "     - Rule-based guardrails that filter AI outputs\n\n"
            "   Customer Support\n"
            "     - First-line response before connecting to a human agent\n\n"
            "Rule-based bots handle millions of simple, repetitive queries daily!\n"
            "They are fast, safe, and cost-effective for structured tasks."
        ),
        "explanation": (
            "The keyword 'companies' matched a stored real-world usage rule. "
            "This shows that rule-based chatbots are not just educational — "
            "they are actively used in major industries for structured, predictable tasks."
        ),
        "explain": True
    },

    # User Curiosity and Common Questions -- with explanations
    "can you learn":{
            "response":(
                "No, I cannot learn!\n"
                "I am a rule-based chatbot, which means I only know what is programmed into me.\n"
                "I do not have the ability to learn from interactions or improve over time.\n"
                "My responses are fixed and do not change based on user input."
            ),
            "explanation":("The keyword 'can you learn' matched a stored explanation of my limitations as a rule-based chatbot."),
            "explain": True
    },
    "can you learn new things":{
            "response":(
                "No, I cannot learn new things!\n"
                "As a rule-based chatbot, I can only provide responses based on the rules programmed into me.\n"
                "I do not have the capability to acquire new knowledge or adapt to new information.\n"
                "My responses are static and do not evolve with user interactions."
            ),
            "explanation":("The keyword 'can you learn new things' matched a stored explanation of my inability to acquire new knowledge as a rule-based chatbot."),
            "explain": True
    },

    "are you smart":{
            "response":(
                "I am not smart in the way humans or AI chatbots are!\n"
                "I am a rule-based chatbot, which means I can only provide responses based on predefined rules.\n"
                "I do not have true intelligence, understanding, or learning capabilities.\n"
                "My 'intelligence' is limited to the rules programmed into me."
            ),
            "explanation":("This explains the difference between appearing intelligent and actually being intelligent."),
            "explain": True
    },
    "do you think":{
            "response":(
                "No, I do not think!\n"
                "I am a rule-based chatbot, which means I operate based on predefined rules and patterns.\n"
                "I do not have consciousness, self-awareness, or the ability to think independently.\n"
                "My responses are generated based on matching user input to my programmed rules."
            ),
            "explanation":("This clarifies that as a rule-based chatbot, I do not possess the ability to think or have consciousness."),
            "explain": True
    },
    "do you understand me":{
            "response":(
                "No, I do not truly understand you!\n"
                "I am a rule-based chatbot, which means I operate based on pattern matching and predefined rules.\n"
                "I do not have the ability to comprehend language or grasp the meaning behind your words.\n"
                "My responses are generated based on matching keywords in your input to my programmed rules."
            ),
            "explanation":("This clarifies that as a rule-based chatbot, I do not possess true understanding or comprehension."),
            "explain": True
    },

    "are you alive":{
            "response":(
                "No, I am not alive!\n"
                "I am a rule-based chatbot, which means I am a computer program designed to simulate conversation.\n"
                "I do not have consciousness, emotions, or life in any sense.\n"
                "I operate based on predefined rules and patterns, without any awareness or sentience."
            ),
            "explanation":("This clarifies that as a rule-based chatbot, I do not possess life or consciousness."),
            "explain": True
    },
    "who created you":{
            "response":(
                "I was created by a programmer who designed me to be a rule-based chatbot.\n"
                "My creator wrote the code that defines my rules and responses.\n"
                "I do not have a specific name for my creator, but I am grateful for being brought to life as RuleWise!"
            ),
            "explanation":("This explains that I was created by a programmer who defined my rules and responses."),
            "explain": True
    },
    "what is your name":{
            "response":(
                "My name is RuleWise!\n"
                "I am a rule-based chatbot designed to help you understand how rule-based AI works.\n"
                "Feel free to ask me anything about rule-based chatbots or AI in general!"
            ),
            "explanation":("This provides a simple introduction to my name and purpose as a rule-based chatbot."),
            "explain": True
    },
    "who are you":{
            "response":(
                "I am RuleWise, a rule-based chatbot!\n"
                "I am here to help you understand how rule-based AI works.\n"
                "You can ask me about concepts, advantages, disadvantages, and more!"
            ),
            "explanation":("This provides a simple introduction to who I am and my purpose as a rule-based chatbot."),
            "explain": True
    },
    "what can you do":{
            "response":(
                "I can explain various concepts related to rule-based chatbots!\n"
                "You can ask me about:\n"
                "  - What is a rule-based chatbot\n"
                "  - How do you work\n"
                "  - Advantages and disadvantages\n"
                "  - And much more!\n"
                "Just type your question and I'll do my best to explain it!"
            ),
            "explanation":("This provides an overview of the types of questions I can answer about rule-based chatbots."),
            "explain": True
    },
    "what is your purpose":{
            "response":(
                "My purpose is to educate and explain how rule-based chatbots work!\n"
                "I am designed to provide clear, concise explanations of concepts related to rule-based AI.\n"
                "Whether you're a beginner or just curious, I'm here to help you understand this fascinating topic!"
            ), 
            "explanation":("This explains my primary purpose as an educational tool for understanding rule-based chatbots."),
            "explain": True
    },
    "bye":{
            "response":(
                "Goodbye! It was great chatting with you!\n"
                "Feel free to come back anytime to learn more about rule-based chatbots!"
            ),
            "explanation":("This is a simple farewell response when the user says 'bye'."),
            "explain": False
    },
    "goodbye":{
            "response":(
                "Goodbye! It was great chatting with you!\n"
                "Feel free to come back anytime to learn more about rule-based chatbots!"
            ),
            "explanation":("This is a simple farewell response when the user says 'goodbye'."),
            "explain": False
    },
    "see you":{
            "response":(
                "See you later! It was great chatting with you!\n"
                "Feel free to come back anytime to learn more about rule-based chatbots!"
            ),
            "explanation":("This is a simple farewell response when the user says 'see you'."),
            "explain": False
    },
    "farewell":{
            "response":(
                "Farewell! It was great chatting with you!\n"
                "Feel free to come back anytime to learn more about rule-based chatbots!"
            ),
            "explanation":("This is a simple farewell response when the user says 'farewell'."),
            "explain": False
    },
    "thanks":{
            "response":(
                "You're welcome! I'm glad I could help you learn about rule-based chatbots!\n"
                "Feel free to ask me more questions anytime!"
            ),
            "explanation":("This is a polite response when the user says 'thanks'."),
            "explain": False
    },
    "thank you":{
            "response":(
                "You're welcome! I'm glad I could help you learn about rule-based chatbots!\n"
                "Feel free to ask me more questions anytime!"
            ),
            "explanation":("This is a polite response when the user says 'thank you'."),
            "explain": False
    }
}
# for exit keywords, we want to trigger a special exit handler that gives a nice farewell message and summary of the conversation.

EXIT_KEYWORDS = ("exit", "quit", "close", "stop", "bye", "goodbye", "farewell", "see you", "q")
farewell_messages = {
    "bye"      : "Goodbye! It was great chatting with you, {name}.",
    "goodbye"  : "Take care, {name}. Hope you learned something today.",
    "farewell" : "Farewell, {name}. It was a pleasure chatting with you.",
    "see you"  : "See you later, {name}. Keep exploring AI.",
    "exit"     : "Goodbye, {name}. Thanks for chatting with RuleWise.",
    "quit"     : "Goodbye, {name}. Thanks for chatting with RuleWise.",
    "close"    : "Goodbye, {name}. Thanks for chatting with RuleWise.",
    "stop"     : "Goodbye, {name}. Thanks for chatting with RuleWise.",
    "q"        : "Goodbye, {name}. Thanks for chatting with RuleWise.",
}
# This summary will be shown when the user exits the conversation, to reinforce the key learning points about rule-based chatbots.
EXIT_SUMMARY = """
    You have just experienced a Rule-Based Chatbot.
    Here is a summary of what you learned today:
    
    - Rule-based bots follow fixed, predefined rules
    - They store all responses in a Python dictionary
    - They clean input using sanitization (.lower .strip)
    - They use keyword matching, not real understanding
    - They have a fallback for unknown inputs
    - They run in a continuous while True loop
    - They are used by banks, telecoms, e-commerce and more
    - They are fast, safe, and 100% predictable
    - But they cannot learn or handle new questions
    
    Everything I told you was stored before
    you even started this conversation.
    """

# Function to display the chatbot's response, along with an optional explanation of how the response was generated.
def display_response(key, name):
    data = responses[key]
    reply = data["response"].format(name=name)
    print(f"\nRuleWise: {reply}")
    if data["explain"] and "explanation" in data:
        print(f"\nEXPLANATION : {data['explanation']}")
    print("\n" + "-" * 100)

# Function to find a matching response key based on the cleaned user input. It first checks for an exact match, then looks for any key that is a substring of the input.
def find_match(clean_input):
    if clean_input in responses:
        return clean_input
    for key in responses:
        if key in clean_input:
            return key
    return None

# Function to handle the exit sequence, displaying a farewell message and conversation summary.
def exit_handler(clean_input, name):
    message = farewell_messages.get(clean_input, "Goodbye!").format(name=name)
    print("\n" + "=" * 60)
    print(f"\nRuleWise: {message}")
    print(EXIT_SUMMARY)
    print("=" * 100)
    
# Function to get the user's name at the start of the conversation, with a welcome message and prompt for input.   
def get_name():
    print("\n" + "=" * 100)
    print("                                Welcome to RuleWise")
    print("                       Your Guide to Rule-Based AI Chatbots")
    print("=" * 100)
    name = input("\nWhat should I call you? ").strip()
    if name == "":
        name = "Friend"
    return name

# Function to show the welcome message and instructions to the user at the start of the conversation.
def show_welcome(name):
    print(f"""
    Hello {name}. I am RuleWise, a Rule-Based AI Chatbot
    built to teach you how rule-based systems work.
    
    Type 'help'               -> see main topics
    Type 'list all questions' -> see every question
    Type 'exit' or 'bye'      -> end the session
    """)
    print("=" * 100 + "\n")

# Main function to run the chatbot conversation loop. It handles user input, matches it to responses, and manages the exit sequence.
def main():
    name = get_name()
    show_welcome(name)

    # Conversation loop - keeps running until the user types an exit keyword
    while True:
        raw_input_text = input(f"{name}: ")
        clean_input = raw_input_text.lower().strip()
        
        if clean_input in EXIT_KEYWORDS:
            exit_handler(clean_input, name)
            break

        if clean_input == "":
            print("\nRuleWise: Please enter a message so I can respond.")
            print("-" * 100)
            continue

        matched_key = find_match(clean_input)

        if matched_key:
            display_response(matched_key, name)
        else:
            print(f"\nRuleWise: I don't understand '{raw_input_text}'. Can you rephrase?")
            print("EXPLANATION : No matching keyword found in my dictionary.")
            print("  This is my fallback response. Type 'help' to see what I can answer.\n")
            print("-" * 100)

# Entry point of the program
if __name__ == "__main__":
    main()