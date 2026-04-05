import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Abdul Rahman | AI/ML Engineer",
  description: "Portfolio of Abdul Rahman - AI/ML Engineer, Data Scientist, GenAI Engineer",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
