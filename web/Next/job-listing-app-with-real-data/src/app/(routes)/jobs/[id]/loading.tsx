import { Button } from "@/components/ui/button";
import { ArrowLeft, Loader2 } from "lucide-react";
import Link from "next/link";

export default function Loading() {
	return (
		<div className="container mx-auto py-8 px-4">
			<Button
				variant="ghost"
				asChild
				className="mb-4 pl-0 flex items-center gap-1"
			>
				<Link href="/">
					<ArrowLeft className="h-4 w-4" />
					Back to listings
				</Link>
			</Button>

			<div className="flex flex-col items-center justify-center h-[calc(100vh-200px)] w-full rounded-lg bg-slate-50 border border-slate-200">
				<Loader2 className="h-12 w-12 text-blue-500 animate-spin mb-4" />
				<h3 className="text-lg font-medium text-slate-700">
					Loading job details...
				</h3>
				<p className="text-slate-500 mt-2">
					Please wait while we fetch the information
				</p>
			</div>
		</div>
	);
}
