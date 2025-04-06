import { Skeleton } from "@/components/ui/skeleton";

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

			<div className="grid grid-cols-1 gap-4">
				{Array(5)
					.fill(0)
					.map((_, index) => (
						<Skeleton
							key={index}
							className="h-32 w-full rounded-lg"
						/>
					))}
			</div>
		</div>
	);
}
