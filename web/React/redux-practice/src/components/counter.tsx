import { useSelector, useDispatch } from "react-redux";
import { decrement, increment } from "../app/features/counter/counter-slice";

const Counter = () => {
	const count = useSelector((state) => state.counter.value);
	const dispatch = useDispatch();

	return (
		<div>
			<div>
				<button onClick={() => dispatch(decrement())}>-</button>
				<h1>{count}</h1>
				<button onClick={() => dispatch(increment())}>+</button>
			</div>
		</div>
	);
};

export default Counter;
