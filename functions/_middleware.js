// One canonical host: www.appleorchard.in -> appleorchard.in (301, keeps path and query).
export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (url.hostname === "www.appleorchard.in") return Response.redirect("https://appleorchard.in" + url.pathname + url.search, 301);
  return context.next();
}
