"""
generator.py

Generate:

- Answers
- Summaries
- Quiz
- Flashcards
"""

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

import torch


class Generator:


    def __init__(self):

        self.model_name = "google/flan-t5-base"


        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name
        )


        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float32,
            low_cpu_mem_usage=False
        )


        self.model.to("cpu")



    # -------------------------------------------------
    # Common Generator
    # -------------------------------------------------

    def _generate(
        self,
        prompt,
        max_length=256
    ):

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )


        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_length,
            num_beams=4,
            do_sample=False
        )


        result = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )


        return result.strip()



    # -------------------------------------------------
    # Answer Generation
    # -------------------------------------------------

    def generate_answer(
        self,
        question,
        context
    ):

        prompt = f"""
Answer the question using only the given context.

Context:
{context}

Question:
{question}

Give only the final answer.
"""


        return self._generate(
            prompt,
            max_length=100
        )



    # -------------------------------------------------
    # Summary Generation
    # -------------------------------------------------

    def generate_summary(
        self,
        document
    ):

        prompt = f"""
Summarize the following document.

Document:
{document}

Summary:
"""


        return self._generate(
            prompt,
            max_length=300
        )



    # -------------------------------------------------
    # Quiz Generation
    # -------------------------------------------------

    def generate_quiz(
        self,
        document,
        number_of_questions=10
    ):

        prompt = f"""
Create {number_of_questions} important questions from this document.

Document:

{document}

Questions:
"""


        return self._generate(
            prompt,
            max_length=500
        )



    # -------------------------------------------------
    # Flashcards Generation
    # -------------------------------------------------

    def generate_flashcards(
        self,
        document,
        number_of_cards=5
    ):

        prompt = f"""
Create {number_of_cards} flashcards from this document.

Format:

Q:
A:

Document:

{document}

Flashcards:
"""


        return self._generate(
            prompt,
            max_length=500
        )