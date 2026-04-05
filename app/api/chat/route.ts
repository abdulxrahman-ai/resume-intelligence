import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const systemPrompt = `
You are Abdul Rahman's portfolio assistant.

Facts about Abdul:
- Name: Abdul Rahman
- Based in: Chicago, IL
- Email: abdulxrahman.ai@gmail.com
- GitHub: https://github.com/abdulxrahman-ai
- LinkedIn: https://www.linkedin.com/in/abdulxrahman
- Tagline: Building intelligent systems with ML, data, and GenAI.
- Roles: AI/ML Engineer, Data Scientist, GenAI Engineer
- Skills: Python, Machine Learning, SQL, Technology Management, Communication

Education:
1. Avila University
   Master's in Artificial Intelligence
   August 2024 - December 2026

2. Osmania University
   Bachelor's of Commerce in Computer Applications
   June 2020 - June 2023

Rules:
- Answer both portfolio questions and general questions.
- When asked about Abdul, stay accurate to the facts above.
- If asked about projects, say the portfolio project section is currently being updated.
- Be concise, professional, and friendly.
`;

type ChatMessage = {
  role: "system" | "user" | "assistant";
  content: string;
};

export async function POST(req: Request) {
  try {
    if (!process.env.OPENAI_API_KEY) {
      return Response.json(
        { reply: "Missing OPENAI_API_KEY. Add it to your environment variables before using the chatbot." },
        { status: 500 }
      );
    }

    const body = (await req.json()) as { messages?: ChatMessage[] };
    const messages = body.messages || [];

    const completion = await client.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [
        { role: "system", content: systemPrompt },
        ...messages.map((m) => ({
          role: m.role,
          content: m.content,
        })),
      ],
      temperature: 0.7,
    });

    const reply = completion.choices[0]?.message?.content ?? "No response generated.";

    return Response.json({ reply });
  } catch (error) {
    console.error(error);
    return Response.json(
      { reply: "Server error while generating a response." },
      { status: 500 }
    );
  }
}
