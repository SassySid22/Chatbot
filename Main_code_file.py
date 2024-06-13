import tkinter as tk
from tkinter import scrolledtext

class Chatbot:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=20)
        self.chat_history.pack(padx=20, pady=20)

        self.user_input = tk.Entry(master, width=60)
        self.user_input.pack(pady=20)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

    
        self.qa_dict = {
            "What are the admission requirements for your university?":
            "The admission requirements vary by program and level. Generally, you will need to submit transcripts, standardized test scores, letters of recommendation, and a personal statement. Specific requirements can be found on our website.",
            
            "How do I apply for admission?":
            "To apply, visit our website and complete the online application form. Make sure to submit all required documents and pay the application fee.",
            
            "what is the application deadline?":
            "Application deadlines depend on the program and level of study. Please check our website for the specific deadlines for the program you are interested in.",
            
            "what are the available scholarships for incoming students?":
            "We offer a range of scholarships based on academic merit, financial need, and other criteria. Details can be found on our scholarship webpage.",
            
            "can I transfer credits from another institution?":
            "Yes, we accept transfer credits from accredited institutions. You will need to submit your transcripts for evaluation to determine which credits can be transferred.",
            
            "how can I check the status of my application?":
            "You can check the status of your application by logging into your applicant portal on our website. You will receive updates there.",
            
            "what is the tuition fee for the upcoming academic year?":
            "Tuition fees vary by program and level. You can find the most up-to-date tuition information on our website or by contacting the admissions office.",
            
            "is there a housing option for international students?":
            "Yes, we offer on-campus housing options for international students. You can apply for housing when you are admitted.",
            
            "can I defer my admission to the next semester?":
            "Admission deferrals are considered on a case-by-case basis. You will need to contact the admissions office to discuss your specific situation.",
            
            "where can I find the brochure regarding admission?":
            "Admission brochures are available on our college website and they are free to access for all."
            
        }

    def send_message(self):
        user_message = self.user_input.get()
        self.user_input.delete(0, tk.END)

        self.display_message(f"User: {user_message}")
        self.generate_response(user_message)

    def generate_response(self, user_message):
        response = self.qa_dict.get(user_message, "I'm not sure how to respond to that, Please visit Sharda.ac.in for more.")
        self.display_message(f"Chatbot: {response}")

    def display_message(self, message):
        self.chat_history.insert(tk.END, f"{message}\n")
        self.chat_history.yview(tk.END)

def main():
    root = tk.Tk()
    root.geometry("600x700")
    chatbot_app = Chatbot(root)
    root.mainloop()

if __name__ == "__main__":
    main()
