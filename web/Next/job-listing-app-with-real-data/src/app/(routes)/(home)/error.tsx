"use client";

import { useEffect } from "react";
import { Button } from "@/components/ui/button";
import { AlertCircle } from "lucide-react";
import Link from "next/link";

interface ErrorProps {
	error: Error & { digest?: string };
	reset: () => void;
}

export default function Error({ error, reset }: ErrorProps) {
	useEffect(() => {
		// Log the error to an error reporting service
		console.error("Jobs loading error:", error);
	}, [error]);

	return (
		<div className="container mx-auto py-16 px-4 flex flex-col items-center justify-center min-h-[60vh]">
			<AlertCircle className="h-16 w-16 text-red-500 mb-6" />
			<h2 className="text-2xl font-bold mb-4">Failed to load jobs</h2>
			<p className="text-muted-foreground mb-6 text-center max-w-md">
				We encountered an error while loading the job listings. This
				could be due to a network issue or a problem with our servers.
			</p>
			<div className="flex flex-col sm:flex-row gap-4">
				<Button onClick={() => reset()} variant="default">
					Try again
				</Button>
				<Button variant="outline" asChild>
					<Link href="/">Return to home</Link>
				</Button>
			</div>
		</div>
	);
}
