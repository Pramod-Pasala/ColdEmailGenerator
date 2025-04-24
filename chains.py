import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

class Chain:
    def __init__(self, model_name: str = "llama3-70b-8192" , key: str = os.getenv("GROQ_API_KEY"),temperature: float = 0):
        self.llm = ChatGroq(model_name=model_name, groq_api_key=key, temperature=temperature)

    def extract_job_info(self,job_description: str) -> dict:
        extract_prompt = PromptTemplate.from_template(
                """### SCRAPED TEXT FROM WEB PAGE:
                {page_data}
                ### TASK:
                Scraped text from a web page is provided. Create a json object with the following fields:
                - role: The role of the job
                - experience: The experience required for the job
                - skills: The skills required for the job
                - description: The description of the job
                Only return the json object without any additional text.
                ### JSON OBJECT (NO PREAMBLE TEXT):
                """
            )
        chain_extract = extract_prompt | self.llm
        result = chain_extract.invoke(input = {"page_data":job_description} )
        return eval(result.content)
    
    def write_mail(self, job,links) -> str:
        email_prompt = PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}
                ### BACKGROUND:
                You are Abhi, a Business Development Executive at DIT Technologies that provides various IT solutions.
                Over our experience, we have empowered numerous enterprises with tailored solutions, fostering
                scalability, process optimization, cost reduction, and heightened overall efficiency.
                ### TASK: 
                Your job is to write a cold email to the client regarding the job mentioned above describing
                the capability of DIT Technologies in fulfilling their needs.
                Also add the most relevant ones from the following links to showcase DIT's portfolio:
                {link_list}
                ### Response:
                An email with out any preamble text.
                    
                """
        )
        chain_email = email_prompt | self.llm
        email = chain_email.invoke(input = {"job_description":job, "link_list":links})
        email_content = email.content
        if not email_content.startswith("Subject"):
            email_content = "Subject" + email_content.split("Subject")[1].strip()
        return email_content