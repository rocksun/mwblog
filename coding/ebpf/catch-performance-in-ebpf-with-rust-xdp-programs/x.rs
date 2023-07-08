fn try_fun_xdp(ctx: &XdpContext) -> Result<u32, ()> {
let eth_hdr: *const EthHdr = unsafe { ptr_at(ctx, 0)? };
unsafe {
let EtherType::Ipv4 = (*eth_hdr).ether_type else {
return Ok(xdp_action::XDP_PASS);
};
}
let ipv4_hdr: *const Ipv4Hdr = unsafe { ptr_at(ctx, EthHdr::LEN)? };
let source_addr = unsafe { (*ipv4_hdr).src_addr };
info!(ctx, “IPv4 Source Address: {}”, source_addr);
Ok(xdp_action::XDP_PASS)
}
}
}