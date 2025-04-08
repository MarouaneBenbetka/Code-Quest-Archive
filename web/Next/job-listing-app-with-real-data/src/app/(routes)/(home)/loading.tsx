import { Skeleton } from "@/components/ui/skeleton";
import { Loader2 } from "lucide-react";

export default function Loading() {
	return (
		<div className="container mx-auto py-8 px-4">
			<div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-6">
				<div>
					<Skeleton className="h-8 w-40 mb-2" />
					<Skeleton className="h-4 w-32" />
				</div>
				<Skeleton className="h-10 w-40 mt-4 md:mt-0" />
			</div>

			<div className="flex justify-center my-8">
				<div className="flex flex-col items-center">
					<Loader2 className="h-12 w-12 text-primary animate-spin mb-4" />
					<p className="text-lg font-medium text-muted-foreground">
						Loading jobs...
					</p>
				</div>
			</div>

			<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
				{Array(6)
					.fill(0)
					.map((_, index) => (
						<div
							key={index}
							className="border rounded-lg p-4 shadow-sm"
						>
							<Skeleton className="h-6 w-3/4 mb-4" />
							<Skeleton className="h-4 w-full mb-2" />
							<Skeleton className="h-4 w-2/3 mb-4" />
							<div className="flex justify-between items-center mt-4">
								<Skeleton className="h-5 w-24" />
								<Skeleton className="h-8 w-24 rounded-full" />
							</div>
						</div>
					))}
			</div>
		</div>
	);
}
