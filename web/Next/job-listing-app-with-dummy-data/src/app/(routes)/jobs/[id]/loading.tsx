import { Skeleton } from "@/components/ui/skeleton";
import { Button } from "@/components/ui/button";
import { ArrowLeft } from "lucide-react";
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

			<Skeleton className="h-[calc(100vh-200px)] w-full rounded-lg" />
		</div>
	);
}
