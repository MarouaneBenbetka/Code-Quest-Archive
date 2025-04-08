import { Button } from "@/components/ui/button";
import Link from "next/link";
import { FileQuestion } from "lucide-react";

export default function NotFound() {
	return (
		<div className="container mx-auto py-16 px-4 flex flex-col items-center justify-center text-center">
			<FileQuestion className="h-24 w-24 text-slate-400 mb-6" />
			<h1 className="text-4xl font-bold text-slate-800 mb-4">
				404 - Not Found
			</h1>
			<p className="text-slate-600 mb-8 max-w-md">
				The job you're looking for doesn't exist or has been removed.
			</p>
			<Button asChild>
				<Link href="/">Back to Job Listings</Link>
			</Button>
		</div>
	);
}
