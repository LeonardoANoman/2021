import Loader from "react-loader-spinner";

export const Loading = () => {
  return (
    <div className="flex justifiy-center items-center">
      <Loader type="Puff" color="#00BFFF" height={550} width={80} />
    </div>
  );
};
