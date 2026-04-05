"use client";

import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Bot,
  Brain,
  Briefcase,
  FileText,
  Github,
  Home,
  Linkedin,
  Mail,
  Menu,
  MessageCircle,
  Send,
  Sparkles,
  User,
  X,
} from "lucide-react";

type Message = {
  role: "assistant" | "user";
  content: string;
};

const navItems = [
  { id: "home", label: "Home", icon: Home },
  { id: "about", label: "About", icon: User },
  { id: "projects", label: "Projects", icon: Briefcase },
  { id: "skills", label: "Skills", icon: Brain },
  { id: "resume", label: "Resume", icon: FileText },
  { id: "contact", label: "Contact", icon: Mail },
];

const skills = [
  "Python",
  "Machine Learning",
  "SQL",
  "Technology Management",
  "Communication",
];

const education = [
  {
    school: "Avila University",
    degree: "Master's in Artificial Intelligence",
    field: "Artificial Intelligence",
    dates: "August 2024 – December 2026",
  },
  {
    school: "Osmania University",
    degree: "Bachelor's of Commerce in Computer Applications",
    field: "Commerce",
    dates: "June 2020 – June 2023",
  },
];

const starterMessage =
  "Hi, I’m Abdul’s AI assistant. Ask me about his background, skills, and projects.";

function Section({
  id,
  title,
  eyebrow,
  children,
}: {
  id: string;
  title: string;
  eyebrow: string;
  children: React.ReactNode;
}) {
  return (
    <section id={id} className="scroll-mt-24 py-16 sm:py-20">
      <div className="mb-8">
        <p className="mb-2 text-sm font-medium uppercase tracking-[0.25em] text-slate-500">
          {eyebrow}
        </p>
        <h2 className="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">
          {title}
        </h2>
      </div>
      {children}
    </section>
  );
}

function ChatBot() {
  const [open, setOpen] = useState(false);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    { role: "assistant", content: starterMessage },
  ]);

  const sendMessage = async (preset?: string) => {
    const value = (preset ?? input).trim();
    if (!value || loading) return;

    const nextMessages: Message[] = [
      ...messages,
      { role: "user", content: value },
    ];
    setMessages(nextMessages);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: nextMessages }),
      });

      const data = (await res.json()) as { reply?: string };

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.reply || "Sorry, something went wrong.",
        },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Sorry, I couldn't reach the AI service.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const quickQuestions = [
    "Who is Abdul Rahman?",
    "What are his skills?",
    "What is he studying?",
    "How can I contact him?",
  ];

  return (
    <>
      <motion.button
        whileHover={{ scale: 1.04 }}
        whileTap={{ scale: 0.96 }}
        onClick={() => setOpen((v) => !v)}
        className="fixed bottom-6 right-6 z-50 flex items-center gap-3 rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-900 shadow-2xl shadow-slate-300/30"
      >
        {open ? <X className="h-4 w-4" /> : <MessageCircle className="h-4 w-4" />}
        {open ? "Close chat" : "Ask Abdul AI"}
      </motion.button>

      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0, y: 16, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 12, scale: 0.98 }}
            className="fixed bottom-24 right-6 z-50 flex h-[32rem] w-[23rem] max-w-[calc(100vw-2rem)] flex-col overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-2xl shadow-slate-300/40"
          >
            <div className="border-b border-slate-100 bg-gradient-to-r from-slate-50 to-white p-4">
              <div className="flex items-center gap-3">
                <div className="rounded-2xl bg-slate-900 p-2 text-white">
                  <Bot className="h-5 w-5" />
                </div>
                <div>
                  <h3 className="font-semibold text-slate-900">Abdul’s AI Assistant</h3>
                  <p className="text-xs text-slate-500">Live portfolio chatbot</p>
                </div>
              </div>
            </div>

            <div className="flex-1 space-y-4 overflow-y-auto bg-slate-50/60 p-4">
              {messages.map((message, index) => (
                <div
                  key={`${message.role}-${index}`}
                  className={`max-w-[85%] rounded-2xl px-4 py-3 text-sm leading-relaxed ${
                    message.role === "assistant"
                      ? "bg-white text-slate-700 shadow-sm"
                      : "ml-auto bg-slate-900 text-white"
                  }`}
                >
                  {message.content}
                </div>
              ))}
              {loading && (
                <div className="max-w-[85%] rounded-2xl bg-white px-4 py-3 text-sm text-slate-500 shadow-sm">
                  Thinking...
                </div>
              )}
            </div>

            <div className="border-t border-slate-100 p-4">
              <div className="mb-3 flex flex-wrap gap-2">
                {quickQuestions.map((q) => (
                  <button
                    key={q}
                    onClick={() => void sendMessage(q)}
                    className="rounded-full border border-slate-200 bg-white px-3 py-1.5 text-xs text-slate-700 transition hover:bg-slate-50"
                  >
                    {q}
                  </button>
                ))}
              </div>

              <div className="flex items-center gap-2">
                <input
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") {
                      void sendMessage();
                    }
                  }}
                  placeholder="Ask anything..."
                  className="flex-1 rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none focus:border-slate-300"
                />
                <button
                  onClick={() => void sendMessage()}
                  className="rounded-2xl bg-slate-900 p-3 text-white transition hover:opacity-90"
                >
                  <Send className="h-4 w-4" />
                </button>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}

export default function Page() {
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <div className="min-h-screen bg-white text-slate-700">
      <div className="pointer-events-none fixed inset-0 bg-[radial-gradient(circle_at_top_right,rgba(148,163,184,0.08),transparent_28%),radial-gradient(circle_at_bottom_left,rgba(59,130,246,0.05),transparent_26%)]" />

      <header className="sticky top-0 z-40 border-b border-slate-200/80 bg-white/85 backdrop-blur-xl">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
          <a href="#home" className="flex items-center gap-3 font-semibold tracking-tight text-slate-900">
            <span className="rounded-2xl bg-slate-900 p-2 text-white">
              <Sparkles className="h-4 w-4" />
            </span>
            Abdul Rahman
          </a>

          <nav className="hidden items-center gap-1 md:flex">
            {navItems.map((item) => (
              <a
                key={item.id}
                href={`#${item.id}`}
                className="rounded-full px-4 py-2 text-sm text-slate-600 transition hover:bg-slate-100 hover:text-slate-900"
              >
                {item.label}
              </a>
            ))}
          </nav>

          <button
            onClick={() => setMobileOpen((v) => !v)}
            className="rounded-xl border border-slate-200 p-2 text-slate-700 md:hidden"
          >
            {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
        </div>

        {mobileOpen && (
          <div className="border-t border-slate-200 bg-white md:hidden">
            <div className="mx-auto flex max-w-6xl flex-col px-4 py-3 sm:px-6 lg:px-8">
              {navItems.map((item) => (
                <a
                  key={item.id}
                  href={`#${item.id}`}
                  onClick={() => setMobileOpen(false)}
                  className="rounded-xl px-3 py-3 text-sm text-slate-700 hover:bg-slate-50"
                >
                  {item.label}
                </a>
              ))}
            </div>
          </div>
        )}
      </header>

      <main className="relative mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <Section id="home" eyebrow="AI / ML / GenAI" title="Building intelligent systems with ML, data, and GenAI.">
          <div className="grid items-center gap-8 lg:grid-cols-[1.2fr_0.8fr]">
            <div>
              <p className="max-w-2xl text-lg leading-8 text-slate-600 sm:text-xl">
                I’m <span className="font-semibold text-slate-900">Abdul Rahman</span>, an aspiring AI/ML Engineer and GenAI-focused builder based in Chicago. I enjoy turning data, machine learning, and practical problem-solving into useful digital experiences.
              </p>
              <div className="mt-8 flex flex-wrap gap-3">
                <a href="#projects" className="rounded-full bg-slate-900 px-6 py-3 text-sm font-medium text-white transition hover:opacity-90">
                  View Projects
                </a>
                <a href="/resume.pdf" className="rounded-full border border-slate-300 px-6 py-3 text-sm font-medium text-slate-800 transition hover:bg-slate-50">
                  Download Resume
                </a>
              </div>
              <div className="mt-10 flex flex-wrap gap-3">
                {skills.map((skill) => (
                  <span key={skill} className="rounded-full border border-slate-200 bg-white px-4 py-2 text-sm text-slate-700 shadow-sm">
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            <div className="rounded-[2rem] border border-slate-200 bg-gradient-to-br from-white to-slate-50 p-6 shadow-xl shadow-slate-200/60">
              <div className="rounded-[1.5rem] border border-slate-100 bg-white p-6">
                <div className="mb-6 flex items-center gap-3">
                  <div className="rounded-2xl bg-slate-900 p-3 text-white">
                    <Brain className="h-5 w-5" />
                  </div>
                  <div>
                    <p className="font-semibold text-slate-900">Focus Areas</p>
                    <p className="text-sm text-slate-500">Current learning and career direction</p>
                  </div>
                </div>
                <div className="space-y-4 text-sm text-slate-600">
                  <div className="rounded-2xl border border-slate-100 bg-slate-50 p-4">
                    <p className="font-medium text-slate-900">Machine Learning</p>
                    <p className="mt-1">Building a strong base in applied ML, model development, and structured problem solving.</p>
                  </div>
                  <div className="rounded-2xl border border-slate-100 bg-slate-50 p-4">
                    <p className="font-medium text-slate-900">Data + SQL</p>
                    <p className="mt-1">Using data analysis and query skills to support insights, pipelines, and decision-making.</p>
                  </div>
                  <div className="rounded-2xl border border-slate-100 bg-slate-50 p-4">
                    <p className="font-medium text-slate-900">GenAI</p>
                    <p className="mt-1">Exploring practical AI interfaces, assistants, and portfolio-ready product experiences.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </Section>

        <Section id="about" eyebrow="About" title="A focused foundation in AI, data, and problem solving.">
          <div className="grid gap-6 lg:grid-cols-2">
            <div className="rounded-[2rem] border border-slate-200 bg-white p-8 shadow-lg shadow-slate-200/40">
              <p className="text-base leading-8 text-slate-600">
                Abdul Rahman is an aspiring AI/ML Engineer, Data Scientist, and GenAI-focused professional currently based in Chicago, Illinois. He is pursuing a Master&apos;s in Artificial Intelligence at Avila University and building a portfolio centered around machine learning, data-driven thinking, and modern AI experiences. His background combines technical curiosity with communication and technology management, helping him approach problems with both analytical depth and practical clarity.
              </p>
            </div>
            <div className="rounded-[2rem] border border-slate-200 bg-white p-8 shadow-lg shadow-slate-200/40">
              <h3 className="mb-5 text-lg font-semibold text-slate-900">Education</h3>
              <div className="space-y-5">
                {education.map((item) => (
                  <div key={item.school} className="rounded-2xl border border-slate-100 bg-slate-50 p-5">
                    <p className="font-semibold text-slate-900">{item.school}</p>
                    <p className="mt-1 text-sm text-slate-700">{item.degree}</p>
                    <p className="mt-1 text-sm text-slate-500">{item.field}</p>
                    <p className="mt-2 text-sm text-slate-500">{item.dates}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </Section>

        <Section id="projects" eyebrow="Projects" title="Project space ready for future work.">
          <div className="rounded-[2rem] border border-dashed border-slate-300 bg-slate-50 p-10 text-center">
            <p className="text-lg font-medium text-slate-900">Projects will be added here.</p>
            <p className="mx-auto mt-3 max-w-2xl text-slate-600">
              This section is intentionally left open so new AI, ML, data, or GenAI projects can be inserted later.
            </p>
          </div>
        </Section>

        <Section id="skills" eyebrow="Skills" title="Core strengths being built and applied.">
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {skills.map((skill) => (
              <div key={skill} className="rounded-[1.75rem] border border-slate-200 bg-white p-6 shadow-lg shadow-slate-200/30">
                <p className="text-lg font-semibold text-slate-900">{skill}</p>
              </div>
            ))}
          </div>
        </Section>

        <Section id="resume" eyebrow="Resume" title="Resume placeholder ready for upload.">
          <div className="rounded-[2rem] border border-slate-200 bg-white p-8 shadow-lg shadow-slate-200/30">
            <p className="max-w-2xl text-slate-600">
              Replace the placeholder <span className="font-medium text-slate-900">resume.pdf</span> file later with your final resume.
            </p>
            <a href="/resume.pdf" className="mt-6 inline-flex rounded-full bg-slate-900 px-6 py-3 text-sm font-medium text-white transition hover:opacity-90">
              Download Resume
            </a>
          </div>
        </Section>

        <Section id="contact" eyebrow="Contact" title="Let’s connect.">
          <div className="rounded-[2rem] border border-slate-200 bg-white p-8 shadow-lg shadow-slate-200/30">
            <div className="mt-2 space-y-4 text-sm text-slate-700">
              <a href="mailto:abdulxrahman.ai@gmail.com" className="flex items-center gap-3 rounded-2xl border border-slate-100 bg-slate-50 px-4 py-4 hover:bg-slate-100">
                <Mail className="h-4 w-4" />
                abdulxrahman.ai@gmail.com
              </a>
              <a href="https://github.com/abdulxrahman-ai" target="_blank" rel="noreferrer" className="flex items-center gap-3 rounded-2xl border border-slate-100 bg-slate-50 px-4 py-4 hover:bg-slate-100">
                <Github className="h-4 w-4" />
                GitHub
              </a>
              <a href="https://www.linkedin.com/in/abdulxrahman" target="_blank" rel="noreferrer" className="flex items-center gap-3 rounded-2xl border border-slate-100 bg-slate-50 px-4 py-4 hover:bg-slate-100">
                <Linkedin className="h-4 w-4" />
                LinkedIn
              </a>
            </div>
          </div>
        </Section>
      </main>

      <footer className="border-t border-slate-200 bg-white">
        <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-3 px-4 py-8 text-sm text-slate-500 lg:flex-row">
          <p>© 2026 Abdul Rahman. Built for AI/ML, data, and GenAI opportunities.</p>
          <div className="flex items-center gap-4">
            <a href="https://github.com/abdulxrahman-ai" target="_blank" rel="noreferrer" className="hover:text-slate-800">
              GitHub
            </a>
            <a href="https://www.linkedin.com/in/abdulxrahman" target="_blank" rel="noreferrer" className="hover:text-slate-800">
              LinkedIn
            </a>
          </div>
        </div>
      </footer>

      <ChatBot />
    </div>
  );
}
