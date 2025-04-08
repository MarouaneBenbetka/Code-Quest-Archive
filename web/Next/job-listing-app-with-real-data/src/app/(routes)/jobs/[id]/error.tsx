"use client";

import { useEffect } from "react";
import { Button } from "@/components/ui/button";
import { AlertOctagon } from "lucide-react";
import Link from "next/link";

interface ErrorProps {
	error: Error & { digest?: string };
	reset: () => void;
}

export default function Error({ error, reset }: ErrorProps) {
	useEffect(() => {
		// Log the error to an error reporting service
		console.error("Single job loading error:", error);
	}, [error]);

	return (
		<div className="container mx-auto py-16 px-4 flex flex-col items-center justify-center min-h-[60vh]">
			<AlertOctagon className="h-16 w-16 text-red-500 mb-6" />
			<h2 className="text-2xl font-bold mb-4">Job details unavailable</h2>
			<p className="text-muted-foreground mb-6 text-center max-w-md">
				We couldn't load the details for this specific job. The job may
				have been removed or there might be a temporary issue with our
				system.
			</p>
			<div className="flex flex-col sm:flex-row gap-4">
				<Button onClick={() => reset()} variant="default">
					Try again
				</Button>
				<Button variant="outline" asChild>
					<Link href="">View all jobs</Link>
				</Button>
			</div>
		</div>
	);
}
