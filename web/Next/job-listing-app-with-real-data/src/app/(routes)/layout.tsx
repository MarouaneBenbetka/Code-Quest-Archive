import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "../../styles/globals.css";
import QueryProvider from "@/components/wrappers/query-provider";
import TopLoaderClient from "@/components/ui/next-client-top-loader";

const geistSans = Geist({
	variable: "--font-geist-sans",
	subsets: ["latin"],
});

const geistMono = Geist_Mono({
	variable: "--font-geist-mono",
	subsets: ["latin"],
});

export const metadata: Metadata = {
	title: "Job Listing App",
	description:
		"This is a job listing app built with Next.js and Tailwind CSS.",
};

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<html lang="en">
			<body
				className={`${geistSans.variable} ${geistMono.variable} antialiased`}
			>
				<QueryProvider>
					<TopLoaderClient />
					{children}
				</QueryProvider>
			</body>
		</html>
	);
}
