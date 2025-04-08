"use client";

import NextTopLoader from "nextjs-toploader";
import { usePathname, useRouter, useSearchParams } from "next/navigation";
import { Suspense, useEffect } from "react";
import NProgress from "nprogress";

const Loader = () => {
	const router = useRouter();

	const { push } = router;

	router.push = (href, options) => {
		NProgress.start();
		push(href, options);
	};

	const pathname = usePathname();
	const searchParams = useSearchParams();

	useEffect(() => {
		NProgress.done();
	}, [pathname, searchParams]);

	return <NextTopLoader color="#5A5A5A" showSpinner={false} shadow={false} />;
};

const TopLoaderClient = () => {
	return (
		<Suspense>
			<Loader />
		</Suspense>
	);
};

export default TopLoaderClient;
