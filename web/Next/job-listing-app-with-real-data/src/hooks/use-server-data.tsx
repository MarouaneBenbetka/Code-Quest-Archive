import {
	HydrationBoundary,
	QueryClient,
	QueryFunction,
	QueryKey,
	dehydrate,
} from "@tanstack/react-query";

interface QueryConfig {
	queryKey: QueryKey;
	queryFn: QueryFunction;
}

type UseServerDataArgs = QueryConfig | QueryConfig[];

export async function useServerData(args: UseServerDataArgs) {
	const queryClient = new QueryClient();

	const prefetchQueries = Array.isArray(args) ? args : [args];

	await Promise.all(
		prefetchQueries.map((query) =>
			queryClient.prefetchQuery({
				queryKey: query.queryKey,
				queryFn: query.queryFn,
			})
		)
	);

	return {
		ServerData: ({ children }: { children: React.ReactNode }) => {
			return (
				<HydrationBoundary state={dehydrate(queryClient)}>
					{children}
				</HydrationBoundary>
			);
		},
	};
}
