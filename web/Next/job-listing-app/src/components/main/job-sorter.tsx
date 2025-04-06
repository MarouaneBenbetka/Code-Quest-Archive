"use client";

import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "@/components/ui/select";

interface JobSorterProps {
	value: string;
	onChange: (value: string) => void;
}

export function JobSorter({ value, onChange }: JobSorterProps) {
	return (
		<div className="flex items-center gap-2">
			<span className="text-sm text-slate-500">Sort by:</span>
			<Select value={value} onValueChange={onChange}>
				<SelectTrigger className="w-[180px]">
					<SelectValue placeholder="Sort by" />
				</SelectTrigger>
				<SelectContent>
					<SelectItem value="most-relevant">Most relevant</SelectItem>
					<SelectItem value="newest">Newest</SelectItem>
					<SelectItem value="oldest">Oldest</SelectItem>
					<SelectItem value="deadline">Deadline</SelectItem>
				</SelectContent>
			</Select>
		</div>
	);
}
