import React, { useMemo, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import {
  ChevronDown,
  FileText,
  BarChart3,
  Lightbulb,
  Target,
  Activity,
  Brain,
  Upload,
  CheckCircle2,
  Sparkles,
  X,
} from "lucide-react";

const navItems = [
  { label: "Overview", icon: FileText },
  { label: "Input", icon: Upload },
  { label: "Results", icon: BarChart3 },
  { label: "Live activity", icon: Activity },
  { label: "Skill cards", icon: Brain },
  { label: "Resume improvements", icon: Lightbulb },
];

const digestCards = [
  {
    title: "ATS fit snapshot",
    description:
      "See how strongly the resume aligns with a target AI/ML role before applying.",
    icon: Target,
  },
  {
    title: "Skill gap analysis",
    description:
      "Identify missing tools, frameworks, and role-specific keywords from the description.",
    icon: Brain,
  },
  {
    title: "Actionable improvements",
    description:
      "Get concrete bullet rewrites and stronger phrasing suggestions for each section.",
    icon: Lightbulb,
  },
  {
    title: "Live review guidance",
    description:
      "Follow the review flow and improve your resume with structured feedback.",
    icon: Activity,
  },
];

const featureCards = [
  {
    title: "Circular metrics",
    body: "Final score, skill fit, semantic fit, and keyword match in one clean summary.",
  },
  {
    title: "Hiring-focused review",
    body: "Highlights strengths, gaps, and the most important improvements for the target role.",
  },
  {
    title: "Valuable updates",
    body: "Transforms generic bullet points into clearer, outcome-driven statements.",
  },
];

const projectOverviewPoints = [
  "I built AI Resume Analyzer to help candidates review their resumes with more clarity before applying.",
  "The project compares a resume against a target role and turns that comparison into structured insights.",
  "Instead of only showing a score, it explains strengths, missing skills, weak phrasing, and practical improvement opportunities.",
  "The goal of the project is to make resume review faster, more actionable, and easier to understand for job seekers.",
];

const howItWorksSteps = [
  "I upload a resume and provide the target job description I want to match.",
  "The system analyzes the content for relevance, skill alignment, keyword coverage, and semantic fit.",
  "It then organizes the findings into a readable dashboard with scores, observations, and improvement cards.",
  "Finally, I use those insights to refine the resume so it is stronger, more role-focused, and more ATS-friendly.",
];

function AboutDropdown({ open, onClose }) {
  return (
    <AnimatePresence>
      {open && (
        <>
          <button
            aria-label="Close About menu overlay"
            className="fixed inset-0 z-30 bg-slate-900/10"
            onClick={onClose}
          />

          <motion.div
            initial={{ opacity: 0, y: 8, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 8, scale: 0.98 }}
            transition={{ duration: 0.18 }}
            className="absolute right-0 top-14 z-40 w-[420px] max-w-[92vw] overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-2xl"
          >
            <div className="flex items-center justify-between border-b border-slate-100 px-5 py-4">
              <div>
                <p className="text-sm font-semibold text-slate-900">About this project</p>
                <p className="mt-1 text-xs text-slate-500">
                  Overview and workflow from the creator&apos;s perspective
                </p>
              </div>
              <button
                onClick={onClose}
                className="rounded-full p-2 text-slate-500 transition hover:bg-slate-100 hover:text-slate-700"
              >
                <X className="h-4 w-4" />
              </button>
            </div>

            <div className="max-h-[70vh] overflow-y-auto px-5 py-5">
              <section>
                <div className="mb-3 flex items-center gap-2">
                  <Sparkles className="h-4 w-4 text-slate-700" />
                  <h3 className="text-sm font-semibold text-slate-900">Project overview</h3>
                </div>
                <div className="space-y-3 text-sm leading-6 text-slate-600">
                  {projectOverviewPoints.map((point) => (
                    <p key={point} className="rounded-2xl bg-slate-50 px-4 py-3">
                      {point}
                    </p>
                  ))}
                </div>
              </section>

              <section className="mt-6">
                <div className="mb-3 flex items-center gap-2">
                  <CheckCircle2 className="h-4 w-4 text-slate-700" />
                  <h3 className="text-sm font-semibold text-slate-900">How it works</h3>
                </div>
                <div className="space-y-3">
                  {howItWorksSteps.map((step, index) => (
                    <div
                      key={step}
                      className="flex gap-3 rounded-2xl border border-slate-100 bg-white px-4 py-3"
                    >
                      <div className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-slate-900 text-xs font-semibold text-white">
                        {index + 1}
                      </div>
                      <p className="text-sm leading-6 text-slate-600">{step}</p>
                    </div>
                  ))}
                </div>
              </section>
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}

function Sidebar() {
  return (
    <aside className="hidden w-[300px] shrink-0 border-r border-slate-200 bg-slate-50 xl:block">
      <div className="sticky top-0 h-screen overflow-y-auto px-6 py-8">
        <h2 className="text-[20px] font-bold tracking-tight text-slate-900">Navigation</h2>
        <p className="mt-4 text-sm leading-7 text-slate-500">
          A structured workspace for reviewing resumes, checking fit, and improving role alignment.
        </p>

        <nav className="mt-6">
          <ul className="space-y-1.5">
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <li key={item.label}>
                  <button className="flex w-full items-center gap-3 rounded-2xl px-3 py-3 text-left text-slate-700 transition hover:bg-white hover:shadow-sm">
                    <Icon className="h-4 w-4" />
                    <span className="text-sm font-medium">{item.label}</span>
                  </button>
                </li>
              );
            })}
          </ul>
        </nav>

        <div className="mt-8 space-y-4">
          <div className="rounded-3xl border border-blue-100 bg-blue-50 px-4 py-4 text-sm leading-7 text-blue-700">
            Role-focused review for AI/ML, Data Science, and Software applications.
          </div>
          <div className="rounded-3xl border border-slate-200 bg-white px-4 py-4 text-sm leading-7 text-slate-500">
            Keep bullet points outcome-driven and tool-specific for stronger resume impact.
          </div>
        </div>

        <div className="mt-8">
          <h3 className="text-[16px] font-semibold text-slate-900">Quick guidance</h3>
          <ul className="mt-4 space-y-3 text-sm leading-7 text-slate-600">
            <li>• Upload a PDF resume</li>
            <li>• Paste a complete role description</li>
            <li>• Review the score and gaps</li>
            <li>• Use the suggestions to strengthen the resume</li>
          </ul>
        </div>
      </div>
    </aside>
  );
}

function Header({ aboutOpen, setAboutOpen }) {
  return (
    <header className="sticky top-0 z-20 border-b border-slate-200 bg-white/90 backdrop-blur">
      <div className="mx-auto flex max-w-[1400px] items-center justify-between px-6 py-4 lg:px-8">
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-2xl bg-slate-900 text-white shadow-sm">
            <FileText className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-semibold tracking-tight text-slate-900">
              AI Resume Analyzer
            </h1>
            <p className="text-xs text-slate-500">Resume review dashboard with structured guidance</p>
          </div>
        </div>

        <div className="relative">
          <button
            onClick={() => setAboutOpen((prev) => !prev)}
            className="inline-flex items-center gap-2 rounded-2xl border border-slate-200 bg-white px-4 py-2.5 text-sm font-medium text-slate-700 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"
          >
            About
            <ChevronDown
              className={`h-4 w-4 transition ${aboutOpen ? "rotate-180" : "rotate-0"}`}
            />
          </button>

          <AboutDropdown open={aboutOpen} onClose={() => setAboutOpen(false)} />
        </div>
      </div>
    </header>
  );
}

function HeroSection() {
  return (
    <section className="rounded-[32px] border border-slate-200 bg-white p-6 shadow-sm lg:p-8">
      <div className="inline-flex rounded-full border border-blue-200 bg-blue-50 px-4 py-2 text-sm font-medium text-blue-700">
        Resume review workflow
      </div>

      <div className="mt-5 max-w-4xl">
        <h2 className="text-4xl font-bold tracking-tight text-slate-900 lg:text-6xl">
          Faster resume reviews with actionable insights
        </h2>
        <p className="mt-5 max-w-3xl text-base leading-8 text-slate-600 lg:text-lg">
          Upload a resume, compare it against a target role, and review fit, score
          breakdowns, missing signals, and concrete updates that improve quality.
        </p>
      </div>

      <div className="mt-8 flex flex-wrap gap-3">
        <button className="rounded-2xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white shadow-sm transition hover:-translate-y-0.5 hover:shadow-md">
          Review Resume
        </button>
        <button className="rounded-2xl border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 transition hover:-translate-y-0.5 hover:shadow-md">
          Get Insights
        </button>
      </div>
    </section>
  );
}

function DigestCards() {
  return (
    <section className="mt-6 grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-4">
      {digestCards.map((card) => {
        const Icon = card.icon;
        return (
          <motion.div
            key={card.title}
            whileHover={{ y: -4 }}
            transition={{ duration: 0.16 }}
            className="rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm"
          >
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-slate-100 text-slate-700">
              <Icon className="h-5 w-5" />
            </div>
            <h3 className="mt-4 text-base font-semibold text-slate-900">{card.title}</h3>
            <p className="mt-2 text-sm leading-7 text-slate-600">{card.description}</p>
          </motion.div>
        );
      })}
    </section>
  );
}

function FeaturesSection() {
  return (
    <section className="mt-6 rounded-[32px] border border-slate-200 bg-white p-6 shadow-sm lg:p-8">
      <h3 className="text-2xl font-semibold tracking-tight text-slate-900">What you will get</h3>
      <p className="mt-3 max-w-4xl text-sm leading-7 text-slate-600 lg:text-base">
        A concise overview, circular metrics, separate skill cards, live update guidance,
        and structured recommendations that help improve alignment for the target role.
      </p>

      <div className="mt-6 space-y-4">
        {featureCards.map((feature) => (
          <motion.div
            key={feature.title}
            whileHover={{ y: -2 }}
            transition={{ duration: 0.15 }}
            className="rounded-[24px] border border-slate-200 bg-slate-50 px-5 py-5"
          >
            <h4 className="text-base font-semibold text-slate-900">{feature.title}</h4>
            <p className="mt-2 text-sm leading-7 text-slate-600">{feature.body}</p>
          </motion.div>
        ))}
      </div>
    </section>
  );
}

export default function App() {
  const [aboutOpen, setAboutOpen] = useState(false);

  const pageTitle = useMemo(() => "AI Resume Analyzer", []);

  return (
    <div className="min-h-screen bg-slate-100 text-slate-900">
      <Header aboutOpen={aboutOpen} setAboutOpen={setAboutOpen} />

      <div className="mx-auto flex max-w-[1400px]">
        <Sidebar />

        <main className="min-w-0 flex-1 px-5 py-6 lg:px-8 lg:py-8">
          <div className="mb-5 text-sm text-slate-500">
            Dashboard / Resume Review / <span className="font-medium text-slate-700">Current Session</span>
          </div>

          <div className="mb-6 lg:hidden">
            <h2 className="text-2xl font-bold tracking-tight text-slate-900">{pageTitle}</h2>
            <p className="mt-2 text-sm leading-7 text-slate-600">
              Resume review dashboard with structured metrics and improvement guidance.
            </p>
          </div>

          <HeroSection />
          <DigestCards />
          <FeaturesSection />
        </main>
      </div>
    </div>
  );
}
